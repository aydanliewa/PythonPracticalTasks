number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
number3=float(input("Enter the third number: "))
if number1 >= number2 and number1 >= number3:
    print(number1, "is the greatest")
elif number2 >= number1 and number2 >= number3:
    print(number2, "is the greatest")
else:
    print(number3, "is the greatest")