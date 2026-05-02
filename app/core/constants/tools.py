from typing import List

tools: List[dict] = [
    {
        "type": "function",
        "function": {
            "name": "read_by_id",
            "description": "Busca uma conversa no banco pelo ID da conversa.",
            "parameters": {
                "type": "object", 
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "ID da conversa no banco"
                    }
                },
                "required": ["id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_all",
            "description": "Lista todas as conversas salvas no banco de dados.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]
    