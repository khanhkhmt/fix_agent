import os
import requests
from bs4 import BeautifulSoup
from ddgs import DDGS

from config.logger import setup_logging
from plugins_func.register import register_function, ToolType, ActionResponse, Action
from core.utils.cache.manager import cache_manager, CacheType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.connection import ConnectionHandler

TAG = __name__
logger = setup_logging()

WEB_SEARCH_FUNCTION_DESC = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": (
            "联网搜索实时信息。适合价格、新闻、人物职务、比赛结果、政策变动等需要最新事实的问题。"
            "当用户的问题包含今天、最新、现在、实时、目前等时间敏感信息时优先使用。"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "要搜索的问题，例如：今日黄金价格、越南胡志明天气、越南国家主席是谁",
                },
                "count": {
                    "type": "integer",
                    "description": "搜索结果数量，建议1到5，默认3",
                },
                "deep_search": {
                    "type": "boolean",
                    "description": "是否读取正文并聚合多个来源，默认false。复杂问题可设为true。",
                },
                "lang": {
                    "type": "string",
                    "description": "用户语言code，例如zh_CN/vi_VN/en_US，默认zh_CN",
                },
            },
            "required": ["query", "lang"],
        },
    },
}


def _build_proxies(proxy_url: str | None):
    if not proxy_url:
        return None
    return {
        "http": proxy_url,
        "https": proxy_url,
    }


def _fetch_page_excerpt(url: str, timeout: float, source_chars: int, proxy_url: str | None):
    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                )
            },
            timeout=timeout,
            proxies=_build_proxies(proxy_url),
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for node in soup(["script", "style", "nav", "footer", "header"]):
            node.decompose()
        text = soup.get_text(separator="\n", strip=True)
        if not text:
            return f"SOURCE: {url}\n[正文为空或无法解析]"
        return f"SOURCE: {url}\n{text[:source_chars]}..."
    except Exception as e:
        return f"SOURCE: {url}\n[读取失败: {str(e)}]"


@register_function("web_search", WEB_SEARCH_FUNCTION_DESC, ToolType.SYSTEM_CTL)
def web_search(
    conn: "ConnectionHandler",
    query: str,
    count: int = 3,
    deep_search: bool = False,
    lang: str = "zh_CN",
):
    query = (query or "").strip()
    if not query:
        return ActionResponse(Action.ERROR, response="搜索关键词不能为空")

    plugin_config = conn.config.get("plugins", {}).get("web_search", {})
    region = plugin_config.get("region", "vn-vi")
    max_results = min(max(int(count or plugin_config.get("max_results", 3)), 1), 5)
    source_chars = int(plugin_config.get("source_chars", 2500))
    timeout = float(plugin_config.get("timeout", 10))
    proxy_url = plugin_config.get("proxy_url") or os.environ.get("SEARCH_PROXY")

    cache_key = f"{query}|{region}|{max_results}|{deep_search}|{source_chars}"
    cached = cache_manager.get(CacheType.INTENT, cache_key, namespace="web_search")
    if cached:
        return ActionResponse(Action.REQLLM, cached, None)

    try:
        with DDGS(proxy=proxy_url) as ddgs:
            results = list(
                ddgs.text(
                    query,
                    region=region,
                    safesearch="moderate",
                    timelimit="w",
                    max_results=max_results,
                )
            )
    except Exception as e:
        return ActionResponse(Action.ERROR, response=f"联网搜索失败: {e}")

    if not results:
        return ActionResponse(
            Action.REQLLM,
            f"没有搜索到与“{query}”相关的结果，请提醒用户换一个更具体的关键词再试。",
            None,
        )

    lines = ["### WEB SEARCH REPORT ###", f"query: {query}", f"lang: {lang}"]
    for idx, item in enumerate(results, start=1):
        lines.append(f"\n[{idx}] {item.get('title', '未知标题')}")
        lines.append(f"URL: {item.get('href', '')}")
        if item.get("body"):
            lines.append(f"摘要: {item.get('body')}")

    if deep_search:
        lines.append("\n### DEEP SEARCH SOURCES ###")
        for item in results:
            href = item.get("href")
            if href:
                lines.append(_fetch_page_excerpt(href, timeout, source_chars, proxy_url))

    report = "\n".join(lines)
    cache_manager.set(CacheType.INTENT, cache_key, report, namespace="web_search")

    prompt = (
        f"请根据以下联网搜索结果，用{lang}回答用户的问题。\n"
        f"用户问题：{query}\n\n"
        f"{report}\n\n"
        "要求：1. 先给结论；2. 明确说明是联网搜索结果；"
        "3. 如果结果可能随时间变化，请提醒用户这是当前搜索到的信息；"
        "4. 如果来源不一致，请指出差异。"
    )
    return ActionResponse(Action.REQLLM, prompt, None)
