import random

def employee_payload():
    return {
        "name": f"TestUser{random.randint(1000,9999)}",
        "email": f"user{random.randint(1000,9999)}@test.com",
        "role": "Engineer"
    }
