FROM python:3.11-slim

# Install system dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements to the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright chromium browser and its dependencies
RUN playwright install chromium
RUN playwright install-deps

# Copy the entire project structure to the container
COPY src/ src/
COPY app.py .

# Set PYTHONPATH to include the src directory for the container
ENV PYTHONPATH=/app

CMD ["python", "app.py"] 