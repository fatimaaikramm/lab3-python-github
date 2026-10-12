def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return ("Error! Denominator cannot be zero.")
    return a / b

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def percentage(a, b):
    return (a / b) * 100

while True:
    print ("Python Calculator:")
    print ("Select operation:")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Even or Odd")
    print ("6. Calcuate Percentage")
    print ("7. Exit")

    choice = input("Enter choice(1-7): ")

    if choice == "7":
        print("Closing the calculator.Goodbye!")
        break

    elif choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a, "+", b, "=", add(a, b))

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a, "-", b, "=", subtract(a, b))

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a, "*", b, "=", multiply(a, b))

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a, "/", b, "=", divide(a, b))

    elif choice == "5":
        num = int(input("Enter a number to check if it is even or odd: "))
        print(num, "is", even_odd(num))

    elif choice == "6":
        total = float(input("Enter the total value: "))
        obtained = float(input("Enter the obtained value: "))
        print("Percentage:", percentage(obtained, total), "%")

    else:
        print("Invalid input")
