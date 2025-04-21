## Task: Build and Run Java Application using Docker (Multi-Stage Build)

This task demonstrates how to build and run a simple Java application using Docker with a multi-stage build approach.

### Files:

- `multistage-java-app`: A basic Java application that prints a message.
- `Dockerfile`: A multi-stage Dockerfile that compiles the Java code in one stage and runs it in a minimal runtime image.

### Steps to Build and Run:

```bash
# Build the Docker image
docker build -t java-app .

# Run the container
docker run -p 8080:8080 java-app
