from enum import Enum

class RoleEnum(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class ToneEnum(str, Enum):
    formal = "formal"
    friendly = "friendly"
    direct = "direct"


class LanguageEnum(str, Enum):
    pt_br = "pt-BR"
    en_us = "en-US"