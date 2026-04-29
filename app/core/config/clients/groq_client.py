from groq import AsyncClient

from app.core.config.settings import settings

client_groq = AsyncClient(api_key=settings.APP_KEY_GROQ)


