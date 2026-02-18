from faker import Faker
import time
import random


def generate_email() -> str:
    faker = Faker()
    return f"garipov_rail_41_{faker.email()}"

def generate_valid_password():
    faker = Faker()
    return f"{faker.password(length=6)}{random.randint(1, 100000)}"

def generate_wrong_password_with_5_symbols():
    faker = Faker()
    return faker.password(length=5)

def generate_wrong_password_with_4_symbols():
    faker = Faker()
    return faker.password(length=4)

def generate_wrong_password_with_1_symbol():
    return random.randint(1, 9)

print(generate_email())
