import redis
import time
import os
import signal
import sys

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
QUEUE_NAME = os.getenv("QUEUE_NAME", "jobs")

r = redis.Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    decode_responses=True
    
)



def process_job(job_id):
    print(f"⚙️ Processing job {job_id}")

    time.sleep(2)  # simulate work

    r.hset(f"job:{job_id}", "status", "completed")

    print(f"✅ Done: {job_id}")



def shutdown(signal_received, frame):
    print("\n🛑 Worker shutting down safely...")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)



print("🚀 Worker started... waiting for jobs")

while True:
    job = r.brpop(QUEUE_NAME, timeout=5)

    if job:
        _, job_id = job
        process_job(job_id)
    else:
        time.sleep(1)