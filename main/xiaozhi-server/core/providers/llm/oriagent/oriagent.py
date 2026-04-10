import json
import requests
from config.logger import setup_logging
from core.providers.llm.base import LLMProviderBase

TAG = __name__
logger = setup_logging()

class LLMProvider(LLMProviderBase):
    def __init__(self, config):
        self.app_id = config.get("app_id", "").strip()
        self.auth_token = config.get("auth_token", "").strip()
        
        # Determine actual token to use. If auth_token exists, use it. Otherwise fallback to app_id
        token_to_use = self.auth_token if self.auth_token else self.app_id
        
        if token_to_use and not token_to_use.startswith("Bearer "):
            self.bearer_token = f"Bearer {token_to_use}"
        else:
            self.bearer_token = token_to_use

        # Format base URL
        self.base_url = config.get("base_url", "https://api.oriagent.com").rstrip("/")
        if not self.base_url.endswith("/v1"):
            self.base_url = f"{self.base_url}/v1"
            
        self.session_conversation_map = {}

    def response(self, session_id, dialogue, **kwargs):
        # Extract the last user message
        last_msg = next(m for m in reversed(dialogue) if m["role"] == "user")
        conversation_id = self.session_conversation_map.get(session_id, "")

        request_json = {
            "query": last_msg["content"],
            "response_mode": "streaming",
            "user": session_id,
            "inputs": {"assistant_name": "H"},
            "conversation_id": conversation_id,
        }

        try:
            with requests.post(
                f"{self.base_url}/chat-messages",
                headers={"Authorization": self.bearer_token, "Content-Type": "application/json"},
                json=request_json,
                stream=True,
            ) as r:
                logger.error(f"Token: {self.bearer_token[:15]}..., Response: {r.status_code}")
                r.raise_for_status()
                for line in r.iter_lines():
                    if line.startswith(b"data: "):
                        try:
                            line_content = line[6:].decode('utf-8')
                            event = json.loads(line_content)
                            
                            # Cache the conversation ID
                            if not conversation_id:
                                cv_id = event.get("conversation_id")
                                if cv_id:
                                    self.session_conversation_map[session_id] = cv_id
                                    conversation_id = cv_id

                            # Filter replace events and emit answers
                            if event.get("event") != "message_replace" and event.get("answer"):
                                yield event["answer"]
                        except json.JSONDecodeError:
                            logger.bind(tag=TAG).error("Oriagent LLM stream parse error.")
                            continue
        except Exception as e:
            logger.bind(tag=TAG).error(f"Oriagent API request error: {str(e)}")
            yield f"【Lỗi kết nối tới Oriagent: {str(e)}】"

    def response_with_functions(self, session_id, dialogue, functions=None):
        for token in self.response(session_id, dialogue):
            yield token, None
