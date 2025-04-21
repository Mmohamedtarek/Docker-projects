## Task: Run a Python Application using Docker

This task demonstrates how to containerize and run a simple Python application using Docker.

### Files:

- `app.py`: A basic Python script that prints a message.
- `Dockerfile`: Used to create a lightweight container image to run the app.

### Steps to Build and Run:

```bash
# Build the Docker image
docker build -t python-app .

# Run the container
docker run -p 6000:6000 python-app

