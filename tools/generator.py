import random


def generate_email():
    return f"garipov_rail_41_{random.randrange(100, 999)}@mail.ru"

def generate_valid_password():
    return f"Passw{random.randint(1, 100000)}"

def generate_wrong_password_with_5_symbols():
    return f"Pass{random.randint(1, 9)}"

def generate_wrong_password_with_4_symbols():
    return f"Pas{random.randint(1, 9)}"

def generate_wrong_password_with_1_symbol():
    return random.randint(1, 9)
