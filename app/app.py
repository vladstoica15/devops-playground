import os
import signal
import sys
from datetime import datetime
from flask import Flask, jsonify, request

APP_NAME = os.getenv("APP_NAME", "devops-playground")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = Flask(__name__)

@app.before_request
def log_request():
    ts = datetime.utcnow().isoformat()
    app.logger.info(
        '%s method=%s path=%s remote=%s ua="%s"',
        ts,
        request.method,
        request.path,
        request.remote_addr,
        request.headers.get("User-Agent", "-"),
    )
import os
import signal
import sys
from datetime import datetime
from flask import Flask, jsonify, request

APP_NAME = os.getenv("APP_NAME", "devops-playground")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = Flask(__name__)

@app.before_request
def log_request():
    ts = datetime.utcnow().isoformat()
    app.logger.info(
        '%s method=%s path=%s remote=%s ua="%s"',
        ts,
        request.method,
        request.path,
        request.remote_addr,
        request.headers.get("User-Agent", "-"),
    )

@app.get("/")
def root():
    return jsonify(
        name=APP_NAME,
        version=APP_VERSION,
        message="Hello from a minimal Flask service",
    ), 200

@app.get("/health")
def health():
    return jsonify(status="ok"), 200


def _handle_shutdown(signum, frame):
    app.logger.info("Received signal %s. Shutting down gracefully...", signum)
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, _handle_shutdown)
    signal.signal(signal.SIGINT, _handle_shutdown)

    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
