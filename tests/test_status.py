from fastapi.testclient import TestClient
from fast_api.main import app
from fast_api.settings import settings

def test_answer():
    client = TestClient(app)
    response = client.get(settings.main_url + "status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    