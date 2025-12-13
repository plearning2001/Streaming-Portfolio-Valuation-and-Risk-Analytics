#!/bin/bash

echo "Waiting for Kafka to be ready..."
sleep 10

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic transactions \
  --partitions 1 \
  --replication-factor 1

echo "Topic created successfully"
