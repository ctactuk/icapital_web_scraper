FROM python:3.11-slim

# Install system dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN playwright install chromium
RUN playwright install-deps

# Copy the entire project structure
COPY src/ src/
COPY app.py .

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH=/app

CMD ["python", "app.py"] 