# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]