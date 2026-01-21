FROM python:3.12-slim

# Basic runtime hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (better layer caching)
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY app/ /app/

# Default port (can be overridden)
ENV PORT=8080
EXPOSE 8080

# Run
CMD ["python", "app.py"]
