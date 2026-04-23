from fastapi import FastAPI
import redis
import uuid
import os

app = FastAPI()

# Environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
QUEUE_NAME = os.getenv("QUEUE_NAME", "jobs")

# Redis connection
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

# Check connection at startup
try:
    r.ping()
    print("✅ Connected to Redis")
except redis.exceptions.ConnectionError:
    print("⚠️ Redis not available, continuing without crash")
#try:
   # r.ping()
  #except redis.exceptions.ConnectionError:
   # raise Exception("Cannot connect to Redis")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush(QUEUE_NAME, job_id)
    r.hset(f"job:{job_id}", "status", "queued")
    return {"job_id": job_id}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    status = r.hget(f"job:{job_id}", "status")
    if not status:
        return {"error": "not found"}
    return {"job_id": job_id, "status": status}