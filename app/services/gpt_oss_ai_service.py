import json

from app.config import settings
from app.clients import CLIENT_GROQ

from app.schemas.chat_completion import (
    ChatCompletionSchema,
    ChoiceSchema,
    ChatCompletionMessageSchema,
    CompletionUsageSchema,
    StructuredOutputSchema
)
from typing import List, Dict


class GptOssAIService:
    def __init__(self):
        self._client = CLIENT_GROQ
        self._ia_model = settings.GPT_OSS
        self._system_prompt = (
            "Voce e um assistente de comunicacao profissional. "
            "Retorne apenas JSON valido, sem markdown e sem texto fora do JSON. "
            "Siga exatamente o schema pedido no response_format. "
            "answer deve ser array de strings com pelo menos um item. "
            "tone deve ser um de: formal, friendly, direct. "
            "language deve ser um de: pt-BR, en-US. "
            "confidence deve ser numero entre 0 e 1. "
            "next_actions deve ser array de strings."
        )
        self._structured_output_schema = {
            "type": "object",
            "properties": {
                "answer": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "tone": {
                    "type": "string",
                    "enum": ["formal", "friendly", "direct"],
                },
                "language": {
                    "type": "string",
                    "enum": ["pt-BR", "en-US"],
                },
                "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                "next_actions": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": ["answer", "tone", "language", "confidence", "next_actions"],
            "additionalProperties": False,
        }

    async def chat_completion(self, prompts: List[Dict] = []) -> ChatCompletionSchema:

        context_response = await self._client.chat.completions.create(
            model=self._ia_model,
            messages=self._build_messages(prompts),
            temperature=0.2,
            max_tokens=500,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "assistant_message",
                    "schema": self._structured_output_schema,
                },
            },
        )

        response = ChatCompletionSchema(
            id=context_response.id,
            model=context_response.model,
            choices=[
                ChoiceSchema(
                    message=ChatCompletionMessageSchema(
                        role=choice.message.role,
                        content=choice.message.content,
                        structured_output=self._parse_structured_output(choice.message.content),
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
    
    def _build_messages(self, prompts: List[Dict]) -> List[Dict]:
        if prompts and prompts[0].get("role") == "system":
            return prompts

        return [{"role": "system", "content": self._system_prompt}, *prompts]
    
    def _parse_structured_output(self, content: str) -> StructuredOutputSchema | None:
        try:
            payload = json.loads(content)
        except (TypeError, json.JSONDecodeError):
            return None

        try:
            return StructuredOutputSchema.model_validate(payload)
        except Exception:
            return None
