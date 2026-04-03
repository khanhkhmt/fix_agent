import os
import time
import uuid
import requests
import asyncio
from datetime import datetime
from core.providers.tts.base import TTSProviderBase
from config.logger import setup_logging

TAG = __name__
logger = setup_logging()

class TTSProvider(TTSProviderBase):
    def __init__(self, config, delete_audio_file):
        super().__init__(config, delete_audio_file)
        self.api_key = config.get("api_key")
        self.voice = config.get("voice", "banmai")
        self.speed = config.get("speed", "0")
        self.api_url = "https://api.fpt.ai/hmi/tts/v5"
        self.audio_file_type = config.get("format", "mp3")

    def generate_filename(self, extension=".mp3"):
        return os.path.join(
            self.output_file,
            f"fpt-tts-{datetime.now().date()}@{uuid.uuid4().hex}{extension}",
        )

    async def text_to_speak(self, text, output_file):
        try:
            if not self.api_key or "你的" in self.api_key:
                raise Exception("FPT API key is not configured")

            headers = {
                "api_key": self.api_key,
                "voice": self.voice,
                "speed": self.speed,
                "Content-Type": "application/x-www-form-urlencoded"
            }
            
            # 1. Gửi yêu cầu khởi tạo TTS
            logger.bind(tag=TAG).info(f"FPT.AI TTS Request: {text}")
            response = requests.post(
                self.api_url,
                headers=headers,
                data=text.encode("utf-8"),
                timeout=20,
            )
            
            if response.status_code != 200:
                raise Exception(f"FPT.AI Request failed with status {response.status_code}: {response.text}")
            
            res_json = response.json()
            if res_json.get("error") != 0:
                raise Exception(f"FPT.AI API Error: {res_json.get('message')}")
            
            async_url = res_json.get("async")
            if not async_url:
                raise Exception("FPT.AI did not return an async audio URL")
            logger.bind(tag=TAG).debug(f"FPT.AI Async URL: {async_url}")

            # 2. Polling (kiểm tra) cho đến khi file sẵn sàng (tối đa 10 giây cho ứng dụng thời gian thực)
            start_time = time.time()
            audio_content = None
            max_wait = 15 # Giới hạn chờ 15 giây để không treo trợ lý quá lâu
            
            while time.time() - start_time < max_wait:
                audio_response = requests.get(async_url, timeout=20)
                if audio_response.status_code == 200:
                    audio_content = audio_response.content
                    break
                # Đợi một chút trước khi thử lại
                await asyncio.sleep(0.5)
            
            if not audio_content:
                raise Exception(f"FPT.AI Polling timeout after {max_wait}s")

            # 3. Lưu hoặc trả về dữ liệu
            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, "wb") as f:
                    f.write(audio_content)
                return output_file
            else:
                return audio_content

        except Exception as e:
            logger.bind(tag=TAG).error(f"FPT.AI TTS Error: {e}")
            raise Exception(f"FPT.AI TTS failed: {e}")
