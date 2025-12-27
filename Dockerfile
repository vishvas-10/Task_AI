# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables to ensure Python output is sent to logs
# and Python doesn't write .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Install system dependencies if needed (e.g., for database drivers)
# slim images need these for some packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the application
COPY . .

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Run Gunicorn
# --workers 2: Low process count to save RAM
# --threads 2: Handles concurrency within those processes
# --worker-class gthread: Required for thread support
# --worker-tmp-dir /dev/shm: Prevents blocking on worker heartbeats in Docker
CMD ["gunicorn", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "2", \
     "--threads", "2", \
     "--worker-class", "gthread", \
     "--worker-tmp-dir", "/dev/shm", \
     "run:app"]