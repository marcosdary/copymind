from fastapi import APIRouter

from app.api.v1.routes import message_route, conversation_route

api_router = APIRouter()

api_router.include_router(message_route.route, prefix="/message")
api_router.include_router(conversation_route.route, prefix="/conversation")
