from confluent_kafka import Consumer
import json

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "risk-group",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["transactions"])

exposure = 0

print("Risk Consumer started...")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    event = json.loads(msg.value().decode("utf-8"))

    exposure += event["price"] * event["qty"]

    print(f"Risk Exposure Updated: {exposure}")
