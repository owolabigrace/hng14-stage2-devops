### api/main.py line X
- Issue: Redis host hardcoded as "localhost"
- Fix: Replaced with environment variable REDIS_HOST

### api/main.py line X
- Issue: No health check endpoint
- Fix: Added /health route for Docker HEALTHCHECK

### requirements.txt
- Issue: Dependencies written on one line
- Fix: Split into separate lines

### .env.example
- Issue: File was empty
- Fix: Added required environment variables

## Frontend app.js
- Issue: API URL hardcoded to localhost
- Fix: Changed to process.env.API_URL

## Worker
- Issue: Could not connect to Redis in container
- Fix: Used REDIS_HOST env variable