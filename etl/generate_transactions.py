import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate fake transactions
def generate_fake_transactions(n=100):
    transactions = []
    
    for _ in range(n):
        transaction = {
            "transaction_id": fake.uuid4(),
            "date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
            "account_number": fake.iban(),
            "transaction_type": random.choice(["Deposit", "Withdrawal", "Transfer", "Payment"]),
            "amount": round(random.uniform(10, 5000), 2),  # Random amount between 10 and 5000
            "currency": random.choice(["USD", "EUR", "CHF", "GBP"]),
            "status": random.choice(["Completed", "Pending", "Failed"]),
            "merchant": fake.company() if random.random() > 0.5 else "N/A",
            "location": fake.city()
        }
        transactions.append(transaction)

    return pd.DataFrame(transactions)

# Generate and save the transactions
df = generate_fake_transactions(500)
df.to_csv("fake_transactions.csv", index=False)

print("✅ Fake transactions generated and saved to fake_transactions.csv")
