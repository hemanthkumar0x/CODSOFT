def calculator():
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("RESULT:", num1 + num2)
    elif op == "-":
        print("RESULT:", num1 - num2)
    elif op == "*":
        print("RESULT:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("RESULT:", num1 / num2)
        else:
            print("ERROR: Division by zero not allowed.")
    else:
        print("Invalid operation!!.")

calculator()
print("Thank you for using the calculator")

