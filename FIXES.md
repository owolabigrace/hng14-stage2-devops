### api/main.py line 6
- Issue: Redis host hardcoded as "localhost"
- Fix: Replaced with environment variable REDIS_HOST and added fallback "redis"

### api/main.py line X
- Issue: No health check endpoint
- Fix: Added /health route for Docker HEALTHCHECK

### requirements.txt
- Issue: Dependencies written on one line
- Fix: Split into separate lines

## File: /api/.env  
- Issue: Secret committed  
- Fix: Removed and replaced with .env.example

### .env.example
- Issue: File was empty
- Fix: Added required environment variables

### File: /api/main.py  
 - Issue: Same Redis localhost misconfiguration  
 - Fix: Updated to use REDIS_HOST and REDIS_PORT environment variables

## Frontend app.js line 6
- Issue: API URL hardcoded to localhost
- Fix: Changed to process.env.API_U

## File: /worker/worker.py
- Line: 5
- Issue: Could not connect to Redis in container because redis uses localhost
- Fix: Used REDIS_HOST env variable