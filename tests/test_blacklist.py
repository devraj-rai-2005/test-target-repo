import pytest
from fastapi.testclient import TestClient
from app.main import app
import threading

client = TestClient(app)

def test_blacklist_flow():
    token = "test-token-123"
    response = client.post("/blacklist/add", json={"token": token, "expires_at": "2025-01-01T00:00:00Z"})
    assert response.status_code == 200
    
    check = client.get(f"/blacklist/check/{token}")
    assert check.json()["blacklisted"] is True

def test_concurrency():
    def add_tokens():
        for i in range(100):
            client.post("/blacklist/add", json={"token": f"t{i}", "expires_at": "2025-01-01T00:00:00Z"})
    
    threads = [threading.Thread(target=add_tokens) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    
    assert client.get("/blacklist/check/t50").json()["blacklisted"] is True