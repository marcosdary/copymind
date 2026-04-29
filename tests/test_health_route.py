from fastapi import status

def test_health_route(client):
    response = client.get(
        ""
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "Copymind",
        "version": "0.0.1"
    }