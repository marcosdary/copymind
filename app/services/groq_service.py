from typing import List, Dict

from app.core.config.deps import client_groq
from app.core.constants import ModelIAEnum
from app.schemas.chat_completion import (
    ChatCompletionSchema,
    ChoiceSchema,
    ChatCompletionMessageSchema,
    CompletionUsageSchema
)


class GroqService:
    def __init__(self):
        self._client = client_groq

    async def chat_completion(self, messages: List[Dict], model: ModelIAEnum) -> ChatCompletionSchema:

        context_response = await self._client.chat.completions.create(
            model=model.value,
            messages=messages,
            temperature=0.2,
            max_tokens=500,
        )

        response = ChatCompletionSchema(
            id=context_response.id,
            model=context_response.model,
            choices=[
                ChoiceSchema(
                    message=ChatCompletionMessageSchema(
                        role=choice.message.role,
                        content=choice.message.content,
                        reasoning=choice.message.reasoning,
                    )
                )
                for choice in context_response.choices
            ],
            usage=CompletionUsageSchema(
                completion_tokens=context_response.usage.completion_tokens,
                prompt_tokens=context_response.usage.prompt_tokens,
                total_tokens=context_response.usage.total_tokens
            )
        )
        return response
    