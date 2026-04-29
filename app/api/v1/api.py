from fastapi import APIRouter

from app.api.v1.routes import message_route

api_router = APIRouter()

api_router.include_router(message_route.route, prefix="/message")
