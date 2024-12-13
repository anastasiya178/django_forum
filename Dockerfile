# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Set the default command for development
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
