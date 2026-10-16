num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %, **, //): ")
match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero")
    case "%":
        if num2 != 0:
            print(num1 % num2)
        else:
            print("Error: Division by zero")
    case "**":
        if num2 >= 0 and num1!= 0:
            print(num1 ** num2)
        else:
            print("Error: Invalid input for exponentiation")
    case "//":
        if num2 != 0:
            print(num1 // num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Error: Invalid operation")