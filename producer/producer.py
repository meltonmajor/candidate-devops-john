import time
import json
from kafka import KafkaProducer
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "metrics"))
from metrics import get_metrics

KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'system-metrics'

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    print(f"Sending metrics to Kafka topic '{TOPIC_NAME}'...")
    while True:
        metric = json.loads(get_metrics())
        producer.send(TOPIC_NAME, metric)
        print(f"Sent: {metric}")
        time.sleep(5)

if __name__ == '__main__':
    main()

