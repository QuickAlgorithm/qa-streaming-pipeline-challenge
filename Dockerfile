FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
COPY ./data /data

