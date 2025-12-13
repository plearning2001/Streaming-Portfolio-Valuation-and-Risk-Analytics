from confluent_kafka import Producer
import json
import time
import random

producer = Producer({"bootstrap.servers": "localhost:9092"})

assets = ["AAPL", "GOOG", "MSFT"]

while True:
    event = {
        "asset": random.choice(assets),
        "price": round(random.uniform(100, 300), 2),
        "qty": random.randint(1, 50)
    }
    print("Hii")

    producer.produce(
        "transactions",
        json.dumps(event).encode("utf-8")
    )
    producer.flush()

    print("Produced:", event)
    time.sleep(2)
