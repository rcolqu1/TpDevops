from fastapi.testclient import TestClient
from app import app

# Crear un cliente para probar la API
client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok",
        "message": "API funcionando correctamente"
    }
