
import uuid
from datetime import datetime, timedelta

import pandas as pd


def create_transaction(sender, receiver, amount, timestamp):
    """Create a single transaction."""
    return {
        "transaction_id": str(uuid.uuid4()),
        "sender_account": sender,
        "receiver_account": receiver,
        "amount": round(amount, 2),
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")
    }


def create_starburst():
    """
    Starburst:
    One account sends money to many different accounts.
    """

    transactions = []

    source = "FRAUD_STAR_001"

    receivers = [
        "ACC1001",
        "ACC1002",
        "ACC1003",
        "ACC1004",
        "ACC1005"
    ]

    start_time = datetime.now()

    for i, receiver in enumerate(receivers):
        transaction = create_transaction(
            source,
            receiver,
            9500 + i * 100,
            start_time + timedelta(seconds=i * 10)
        )

        transactions.append(transaction)

    return transactions


def create_circular_flow():
    """
    Circular flow:
    Account A → B → C → D → A
    """

    transactions = []

    accounts = [
        "FRAUD_CIRC_001",
        "FRAUD_CIRC_002",
        "FRAUD_CIRC_003",
        "FRAUD_CIRC_004"
    ]

    start_time = datetime.now()

    for i in range(len(accounts)):

        sender = accounts[i]
        receiver = accounts[(i + 1) % len(accounts)]

        transaction = create_transaction(
            sender,
            receiver,
            15000,
            start_time + timedelta(seconds=i * 10)
        )

        transactions.append(transaction)

    return transactions


def create_layering():
    """
    Layering:
    Money passes through multiple intermediary accounts.
    """

    transactions = []

    accounts = [
        "FRAUD_LAYER_001",
        "FRAUD_LAYER_002",
        "FRAUD_LAYER_003",
        "FRAUD_LAYER_004",
        "FRAUD_LAYER_005"
    ]

    start_time = datetime.now()

    for i in range(len(accounts) - 1):

        transaction = create_transaction(
            accounts[i],
            accounts[i + 1],
            20000 - i * 1000,
            start_time + timedelta(seconds=i * 10)
        )

        transactions.append(transaction)

    return transactions


# Generate fraud patterns
starburst_transactions = create_starburst()
circular_transactions = create_circular_flow()
layering_transactions = create_layering()


# Combine all fraud transactions
fraud_transactions = (
    starburst_transactions
    + circular_transactions
    + layering_transactions
)


# Convert to DataFrame
fraud_df = pd.DataFrame(fraud_transactions)


# Save fraud transactions
fraud_df.to_csv(
    "data/fraud_transactions.csv",
    index=False
)


print("Fraud pattern generation completed!")
print(f"Total fraud transactions: {len(fraud_df)}")

print("\nFraud transaction patterns:")
print(fraud_df)
