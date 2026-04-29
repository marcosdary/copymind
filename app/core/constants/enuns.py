from enum import Enum

from app.core.config.deps import settings

class RoleEnum(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"

class ToneEnum(str, Enum):
    formal = "formal"
    friendly = "friendly"
    direct = "direct"


class LanguageEnum(str, Enum):
    pt_br = "pt-BR"
    en_us = "en-US"


class ModelIAEnum(str, Enum):
    llama = settings.LLAMA_VERSATILE
    gpt = settings.GPT_OSS
