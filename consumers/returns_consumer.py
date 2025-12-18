from confluent_kafka import Consumer, Producer
import json

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "returns-consumer",
    "auto.offset.reset": "earliest"
})

producer = Producer({"bootstrap.servers": "localhost:9092"})

consumer.subscribe(["transactions"])

last_price = {}   # state: asset → last price

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue

    event = json.loads(msg.value().decode("utf-8"))
    asset = event["asset"]
    price = event["price"]

    if asset in last_price:
        ret = round((price - last_price[asset]) / last_price[asset],2)

        out = {
            "asset": asset,
            "return": ret
        }

        producer.produce(
            "returns_topic",
            json.dumps(out).encode("utf-8")
        )
        producer.flush()

        print("RETURN:", out)

    last_price[asset] = price
