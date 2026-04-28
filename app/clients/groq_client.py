from groq import Groq, AsyncClient

from app.config.settings import settings

CLIENT_GROQ = AsyncClient(api_key=settings.APP_KEY_GROQ)


