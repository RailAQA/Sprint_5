import random


def generate_email():
    return f"garipov_rail_41_{random.randrange(100, 999)}@mail.ru"

def generate_valid_password():
    return f"Passw{random.randint(100, 100000)}"
