FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "__main__.py"]