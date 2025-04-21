# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy source code
COPY . .

# Expose port (adjust as needed)
EXPOSE 6000

# Run the app
CMD ["python" , "app.py"]
