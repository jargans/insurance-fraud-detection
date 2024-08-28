# Use a lightweight Python image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        gcc \
        libmariadb-dev \
        pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code and initialization script
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["sh", "-c", "python init_db.py && python app.py"]
