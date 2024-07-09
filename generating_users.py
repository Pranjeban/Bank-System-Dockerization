from faker import Faker
import json

fake = Faker()

users = []

for _ in range(20):
    user = {
        "account_id": fake.random_int(min=1000, max=9999),
        "name": fake.name(),
        "current_balance": round(fake.random_number(digits=5, fix_len=True) * 0.01, 2),
        "account_city":fake.address()
    }
    users.append(user)

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)
