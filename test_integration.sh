#!/bin/bash
set -e

timeout 60 bash -c '
docker compose up -d --build
sleep 10
curl -f http://localhost:8000/health
docker compose down
'