# Dockerfile for Shieldhood
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy package
COPY . .

# Install Shieldhood in editable mode
RUN pip install -e .

# Create default config
COPY bankr.config.yaml.example bankr.config.yaml

# Run example when container starts
CMD ["python", "example.py"]
