from kafka import KafkaProducer
import pandas as pd
import json
import time

# Load transaction data
df = pd.read_csv("data/fraud_transactions.csv")

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Kafka Producer started...")
print("Sending transactions...\n")

# Send transactions
for _, row in df.iterrows():

    transaction = {
        "transaction_id": row["transaction_id"],
        "sender_account": row["sender_account"],
        "receiver_account": row["receiver_account"],
        "amount": row["amount"],
        "timestamp": row["timestamp"]
    }

    producer.send("transactions", value=transaction)

    print("Sent:", transaction)

    time.sleep(0.5)

producer.flush()
producer.close()

print("\nAll transactions sent successfully!")