def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

def percentage(x, y):
    return (x / y) * 100

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Percentage")

while True:
    choice = int(input("Enter Function (1/2/3/4/5/6): "))
    if choice in [1, 2, 3, 4, 5, 6]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input, Please enter the correct Values.")
            continue

        if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 4:
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == 5:
            print(num1, "**", num2, "=", exponent(num1, num2))
        elif choice == 6:
            print(num1, "/", num2, "*100 =", percentage(num1, num2))
    else:
        print("Please choose a valid operation.")

    next_cal = input("Do you want to continue (y/n): ").lower()
    if next_cal == 'n':
        break
