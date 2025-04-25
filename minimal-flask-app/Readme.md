# 🐍 Minimal Flask App with Optimized Docker Image

This project is a **minimal Flask application** packaged in a **highly optimized Docker image**. It was developed as part of **Lab 4** for learning how to reduce image size, use minimal base images, and deploy micro web services efficiently.

---

## 🎯 Objective (Lab 4)

The main objective of this lab is to:

- Learn how to create a Flask Docker image with the **smallest possible size**.
- Explore minimal Docker images.
- Practice best practices in Dockerfile optimization.
- Build and test a lightweight Flask container.

---

## 📁 Project Structure

minimal-flask-app/ │ ├── app.py # Main Flask application ├── requirements.txt # Python dependencies ├── Dockerfile # Optimized Dockerfile └── README.md # Project documentation


## 🛠️  Step 2: Build the Docker image 

docker build -t minimal-flask-app .


## ▶️  Step 3: Run the container

docker run -p 5000:5000 minimal-flask-app


## 🌐 Step 4: Access the application

Visit the app in your browser at:

http://localhost:5000

You should see:

Hello from a minimal Flask app!

