from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def generate_random_string():
    response = client.get("/strings/random")

    assert response.status_code == 200
    assert "random_string" in response.json()
    assert response.json()["random_string"]
