from fastapi.testclient import TestClient
from main import app
import fakeredis
import pytest

# Mock Redis
@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr("main.r", fake)

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_create_job():
    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()

def test_get_job():
    res = client.post("/jobs")
    job_id = res.json()["job_id"]

    res2 = client.get(f"/jobs/{job_id}")
    assert res2.status_code == 200
    assert res2.json()["status"] == "queued"

    import fakeredis

    def test_redis_mock():
        r = fakeredis.FakeRedis()
        r.set("key", "value")
        assert r.get("key") == b"value"