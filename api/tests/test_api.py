from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_job():
    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()

def test_get_job_not_found():
    res = client.get("/jobs/invalid")
    assert res.status_code == 200
    assert res.json()["error"] == "not found"

def test_health():
    res = client.get("/health")
    assert res.status_code == 200