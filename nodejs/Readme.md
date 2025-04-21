## Task: Run a Node.js Application using Docker

This task demonstrates how to containerize and run a simple Node.js application using Docker.

### Files:

- `server.js`: A basic Node.js script that prints a message.
- `package.json`: Defines the app and start script.
- `Dockerfile`: Used to create the Docker image and run the app.

### Steps to Build and Run:

```bash
# Build the Docker image
docker build -t nodejs-app .

# Run the container
docker run -p 3000:3000 nodejs-app
