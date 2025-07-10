# candidate-devops

## Overview

This project implements a simple pipeline to collect operating system metrics, publish them to a Kafka topic, and consume those events to store them in a PostgreSQL database. The entire system runs via Docker Compose.

The components are:
- **Metrics generator**: A Python script that collects basic system metrics like CPU and memory usage.
- **Kafka producer**: Publishes metrics to a Kafka topic.
- **Kafka consumer**: Reads from the Kafka topic and inserts the metrics into PostgreSQL.
- **Docker Compose**: Manages Kafka, Zookeeper, PostgreSQL, and can be extended to run producer/consumer as services.

## How to Run

1. **Clone the repo (or copy the files locally)**

2. **Start the environment**
   ```bash
   docker compose up -d

