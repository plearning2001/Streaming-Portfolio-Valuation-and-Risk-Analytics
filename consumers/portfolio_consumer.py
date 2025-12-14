from confluent_kafka import Consumer
import json

# 1️⃣ Kafka consumer configuration
consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "portfolio-group",
    "auto.offset.reset": "earliest"
})

# 2️⃣ Subscribe to topic
consumer.subscribe(["transactions"])

portfolio_value = 0

print("Portfolio Consumer started...")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print("Error:", msg.error())
        continue

    # 3️⃣ Deserialize JSON
    event = json.loads(msg.value().decode("utf-8"))

    # 4️⃣ Business logic
    trade_value = event["price"] * event["qty"]
    portfolio_value += trade_value

    print(f"Trade processed: {event}")
    print(f"Total Portfolio Value: {portfolio_value}")
