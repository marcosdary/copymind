from typing import List, Dict
from groq.types.chat import ChatCompletion

from app.core.config.deps import client_groq
from app.core.constants import ModelIAEnum, tools



class GroqService:
    def __init__(self):
        self._client = client_groq

    async def chat_completion(self, messages: List[Dict], model: ModelIAEnum) -> ChatCompletion:

        response = await self._client.chat.completions.create(
            model=model.value,
            messages=messages,
            temperature=0.6,
            max_tokens=500,
            tools=tools
        )

        return response
    