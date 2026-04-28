import json
from typing import Dict, List

from app.clients import CLIENT_GROQ
from app.config import settings
from app.schemas.chat_completion import (
    ChatCompletionMessageSchema,
    ChatCompletionSchema,
    ChoiceSchema,
    CompletionUsageSchema,
)


class LlamaVersatileAIService:
    def __init__(self):
        self._client = CLIENT_GROQ
        self._ia_model = settings.LLAMA_VERSATILE

    async def chat_completion(self, prompts: List[Dict] = []) -> ChatCompletionSchema:
        context_response = await self._client.chat.completions.create(
            model=self._ia_model,
            messages=prompts,
            temperature=0.7,
            max_tokens=256,
        )

        response = ChatCompletionSchema(
            id=context_response.id,
            model=context_response.model,
            choices=[
                ChoiceSchema(
                    message=ChatCompletionMessageSchema(
                        role=choice.message.role,
                        content=choice.message.content,
                    )
                )
                for choice in context_response.choices
            ],
            usage=CompletionUsageSchema(
                completion_tokens=context_response.usage.completion_tokens,
                prompt_tokens=context_response.usage.prompt_tokens,
                total_tokens=context_response.usage.total_tokens,
            ),
        )
        return response

