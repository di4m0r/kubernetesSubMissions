FROM python:3.12-slim

# Damit Logs sofort rausgehen (kein Buffering)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]