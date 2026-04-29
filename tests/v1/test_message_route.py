from fastapi import status

def test_create_message(client):

    payload = {
        "model": "openai/gpt-oss-120b",
        "messages":  [
            {
                "content": "Recebemos sua inscrição para a posição de Analista de Sistemas Jr. e estamos muito felizes pelo seu interesse em fazer parte do nosso time! 🎉",
                "role": "user"
            }
        ]
    }

    response = client.post(
        "/api/v1/message",
        json=payload
    )

    assert response.status_code == status.HTTP_201_CREATED
