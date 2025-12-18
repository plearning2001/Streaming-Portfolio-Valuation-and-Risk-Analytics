from confluent_kafka import Consumer, Producer
import json

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "returns-group",
    "auto.offset.reset": "earliest"
})

producer = Producer({"bootstrap.servers": "localhost:9092"})

consumer.subscribe(["prices"])

last_price = None  # minimal state

while True:
    msg = consumer.poll(1.0)
    if not msg or msg.error():
        continue

    data = json.loads(msg.value().decode())
    price = data["price"]

    if last_price is not None:
        ret = (price - last_price) / last_price

        event = {
            "timestamp": data["timestamp"],
            "return": ret
        }

        producer.produce("returns", json.dumps(event).encode())
        producer.flush()

        print("Return produced:", event)

    last_price = price
