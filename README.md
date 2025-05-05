# DistribuidArch
Testing Distribuid Architecture

This project demonstrates a basic **distributed architecture** using Docker Compose with:

- A **Producer** (Flask API) that sends tasks
- A **Consumer** (Python worker) that processes tasks
- A **Redis** message queue for communication between services


## 🐳 Docker Images
Images are available on Docker Hub:

darkjus/distributed-producer

darkjus/distributed-consumer

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/DistribuidArch.git
cd DistribuidArch


```bash
docker-compose up --build

```bash
curl -X POST http://localhost:5000/add-task \
     -H "Content-Type: application/json" \
     -d '{"task": "Say hello from producer"}'


