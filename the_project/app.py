import os
from flask import Flask
from datetime import datetime, timezone

app = Flask(__name__)

def get_port():
    # PORT aus ENV, default 3000
    port_str = os.getenv("PORT", "3000")
    try:
        return int(port_str)
    except ValueError:
        # Fallback, wenn jemand Unsinn setzt
        return 3000

@app.route("/")
def index():
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    return f"Todo app - {now}\n"

if __name__ == "__main__":
    port = get_port()
    # Log beim Start
    print(f"Server started in port {port}", flush=True)
    # Flask Server starten
    app.run(host="0.0.0.0", port=port)