import random


def generate_hard_password(length=12):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = '\\/:*?"<>|@'

    all_characters = letters + numbers + symbols

    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols),
    ]

    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)


hard_password = generate_hard_password()
print(f"Generated Hard Password: {hard_password}")

custom_length_password = generate_hard_password(16)
print(f"Custom Length Password: {custom_length_password}")
