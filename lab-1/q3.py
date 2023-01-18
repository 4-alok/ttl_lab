# Write a menu driven program of a calculator - Addition, Subtraction, Multiplication, Division, Modulus

def calculator():
    print("Welcome to the Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    choice = int(input("Enter your choice: "))

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if choice == 1:
        print(number1 + number2)
    elif choice == 2:
        print(number1 - number2)
    elif choice == 3:
        print(number1 * number2)
    elif choice == 4:
        print(number1 / number2)
    elif choice == 5:
        print(number1 % number2)
    else:
        print("Invalid choice! Please choose again.")

calculator()