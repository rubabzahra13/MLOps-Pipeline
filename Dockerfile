# Use an official Python runtime as base
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the application files
COPY src/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

# //check
