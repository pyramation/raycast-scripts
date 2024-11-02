FROM python:3.9-slim

WORKDIR /app

# Install make and other build essentials
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create empty .env file if it doesn't exist
RUN touch .env

# Set Python path to include src directory
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Command to run when container starts
CMD ["python", "src/main.py"]