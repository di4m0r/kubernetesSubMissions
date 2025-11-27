import uuid
import time
import signal
from datetime import datetime, timezone

# Zufällige ID beim Start generieren und im Speicher behalten
random_id = str(uuid.uuid4())
print(f"Application started. Generated id: {random_id}", flush=True)

running = True

def handle_sigterm(signum, frame):
    global running
    print("Received SIGTERM, shutting down...", flush=True)
    running = False

# SIGTERM (von Kubernetes beim Beenden) abfangen
signal.signal(signal.SIGTERM, handle_sigterm)

while running:
    # ISO-8601 Timestamp in UTC, wie im Beispiel
    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"{timestamp}: {random_id}", flush=True)
    time.sleep(5)

print("Exited main loop.", flush=True)