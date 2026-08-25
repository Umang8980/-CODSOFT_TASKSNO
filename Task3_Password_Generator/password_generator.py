# CODSOFT Internship - Task 3
# Password Generator

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


print("======================================")
print("       PASSWORD GENERATOR")
print("======================================")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a positive password length.")
    else:
        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")