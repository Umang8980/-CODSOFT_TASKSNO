# CODSOFT Internship - Task 2
# Advance Calculator

import math

print("======================================")
print("       WELCOME TO MY CALCULATOR")
print("======================================")

print("\nSelect the type of calculation:")
print("1. Basic Calculation")
print("2. Trigonometric Calculation")
print("3. Multiplication Table")
print("4. Factorial")
print("5. Power")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nAvailable operators: +  -  *  /  %")
    operator = input("Enter operator: ")

    if operator == "+":
        print("Result:", a + b)

    elif operator == "-":
        print("Result:", a - b)

    elif operator == "*":
        print("Result:", a * b)

    elif operator == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")

    elif operator == "%":
        if b != 0:
            print("Result:", a % b)
        else:
            print("Cannot find remainder with zero.")

    else:
        print("Invalid operator.")

elif choice == 2:
    angle = float(input("Enter angle in degrees: "))

    print("1. sin")
    print("2. cos")
    print("3. tan")

    operator = input("Enter function: ").lower()

    radians = math.radians(angle)

    if operator == "sin":
        print("Result:", math.sin(radians))

    elif operator == "cos":
        print("Result:", math.cos(radians))

    elif operator == "tan":
        print("Result:", math.tan(radians))

    else:
        print("Invalid function.")

elif choice == 3:
    number = int(input("Enter a number: "))

    print(f"\nMultiplication Table of {number}")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

elif choice == 4:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = math.factorial(number)
        print(f"Factorial of {number} = {factorial}")

elif choice == 5:
    base = float(input("Enter base value: "))
    power = float(input("Enter power: "))

    result = math.pow(base, power)

    print("Result:", result)

else:
    print("Invalid choice.")

print("\nThank you for using My Calculator!")
print("Visit Again!")