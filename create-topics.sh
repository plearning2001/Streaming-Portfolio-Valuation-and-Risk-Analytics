#!/bin/bash

echo "Creating Kafka topics..."

kafka-topics \
  --bootstrap-server kafka:9092 \
  --create \
  --if-not-exists \
  --topic transactions \
  --partitions 1 \
  --replication-factor 1

echo "Topics created"
