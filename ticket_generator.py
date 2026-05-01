import random

issues = [
    "Network outage",
    "Slow internet",
    "Login failure",
    "Server down",
    "Email issue"
]

def create_ticket():
    return {
        "id": random.randint(1000, 9999),
        "issue": random.choice(issues),
        "severity": random.randint(1, 10)
    }
