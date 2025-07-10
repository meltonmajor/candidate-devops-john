# candidate-devops

This project demonstrates a simple DevOps pipeline that collects system-level metrics, sends them through a Kafka pipeline, and stores them in a PostgreSQL database. The entire setup is containerized using Docker Compose, making it easy to spin up and test locally.

---

## Project Overview

The goal is to simulate a real-world streaming pipeline using open-source technologies. Here's what it does:

- Collects system metrics like CPU and memory usage.
- Publishes those metrics to a Kafka topic via a producer.
- Consumes the messages from Kafka and stores them in PostgreSQL.
- Orchestrates all services using Docker Compose.

---

## Components

| Component           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `metrics/`          | Gathers system metrics using `psutil` and makes them available to the producer. |
| `producer/`         | Connects to Kafka and sends JSON-formatted metrics to a topic.              |
| `consumer/`         | Listens to Kafka, parses metrics, and inserts them into PostgreSQL.         |
| `docker-compose.yml`| Spins up Kafka, Zookeeper, PostgreSQL, and other services.                  |

---

## Requirements

Before you begin, make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.10+ (for running producer/consumer scripts locally)

---

## How to Run

### 1. Clone the repository

git clone https://github.com/meltonmajor/candidate-devops-john.git
cd candidate-devops-john

2. Build and Start the Services
docker compose up --build

3. Start the Producer and Consumer (in separate terminals)

Terminal 1: Start the Producer
cd producer
python producer.py

Terminal 2: Start the Consumer
cd consumer
python consumer.py


