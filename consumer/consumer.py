import json
import time
import psycopg2
from kafka import KafkaConsumer

KAFKA_TOPIC = 'system-metrics'
KAFKA_BROKER = 'localhost:9092'

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'metrics'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

def create_table_if_not_exists(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMPTZ,
            cpu_percent REAL,
            memory_percent REAL
        );
    """)

def insert_metric(cursor, data):
    cursor.execute("""
        INSERT INTO metrics (timestamp, cpu_percent, memory_percent)
        VALUES (%s, %s, %s);
    """, (data['timestamp'], data['cpu_percent'], data['memory_percent']))

def main():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    print(f"Listening to Kafka topic '{KAFKA_TOPIC}'...")

    conn = None
    while True:
        try:
            if conn is None or conn.closed:
                conn = psycopg2.connect(
                    host=DB_HOST,
                    port=DB_PORT,
                    dbname=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD
                )
            cursor = conn.cursor()
            create_table_if_not_exists(cursor)

            for message in consumer:
                data = message.value
                insert_metric(cursor, data)
                conn.commit()
                print(f"Inserted: {data}")
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()

