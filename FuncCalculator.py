def calculator(a, b, choice):
    if choice == "+":
        return a + b

    elif choice == "-":
        return a - b

    elif choice == "*":
        return a * b

    elif choice == "/":
        return a / b

a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
choice = input("Enter operator: ")

result = calculator(a, b, choice)

print("Result:", result)
