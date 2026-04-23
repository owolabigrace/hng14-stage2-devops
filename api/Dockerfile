
FROM python:3.11.9-slim AS builder

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt


# FINAL STAGE
# =========================
FROM python:3.11.9-slim

WORKDIR /app


RUN useradd -m appuser


COPY --from=builder /root/.local /home/appuser/.local

COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH


ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

USER appuser


EXPOSE 8000


HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]