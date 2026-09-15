
import random
import uuid
from datetime import datetime, timedelta

import pandas as pd


# Number of transactions
NUM_TRANSACTIONS = 100


# Generate account IDs
accounts = [f"ACC{str(i).zfill(4)}" for i in range(1, 21)]


# Generate transactions
transactions = []

start_time = datetime.now()

for i in range(NUM_TRANSACTIONS):

    sender = random.choice(accounts)
    receiver = random.choice(accounts)

    # Make sure sender and receiver are different
    while receiver == sender:
        receiver = random.choice(accounts)

    amount = round(random.uniform(100, 10000), 2)

    timestamp = start_time + timedelta(seconds=i * 10)

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "sender_account": sender,
        "receiver_account": receiver,
        "amount": amount,
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")
    }

    transactions.append(transaction)


# Convert to DataFrame
df = pd.DataFrame(transactions)


# Save transaction data
df.to_csv("data/transactions.csv", index=False)


print("Transaction generation completed!")
print(f"Total transactions: {len(df)}")
print("\nSample transactions:")
print(df.head())

