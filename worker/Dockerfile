FROM python:3.11-slim

WORKDIR /app


RUN useradd -m appuser


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*


USER appuser


HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]