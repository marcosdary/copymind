from fastapi import FastAPI, status
from typing import Dict

from app.api.v1 import api
from app.core.config.deps import settings

app = FastAPI(
    title="Copymind",
    description="API para conversação com IAs",
    version="0.0.1",
)

app.include_router(api.api_router, prefix=settings.API_V1_STR)

@app.get(
        "/", 
        status_code=status.HTTP_200_OK,
        description="Retorna uma mensagem da API, informando nome e versão atual",
        summary="Mensagem da API",
        response_model=Dict[str, str],
        tags=["Health"],
        responses={
            200: {"description": "API online"},
            500: {"description": "Erro interno do servidor."}
        }
    )
def index():
    return {
        "name": "Copymind",
        "version": "0.0.1"
    }


