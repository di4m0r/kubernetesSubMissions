FROM python:3.12-slim

# Logs direkt ausgeben, nicht puffern
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code
COPY app.py .

# Standard-Port (kann aber per ENV überschrieben werden)
ENV PORT=3000

CMD ["python", "app.py"]