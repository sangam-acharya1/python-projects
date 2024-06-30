def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = input("Choose the operation (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == "4":
            print(num1, "/", num2, "=", div(num1, num2))
    else:
        print("Invalid input, please try again.")
