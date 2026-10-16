number1=int(input())
number2=int(input())
number3=int(input())
if number1 >= number2 and number1 >= number3:
    largest = number1
    if number2 >= number3:
        middle = number2
        smallest = number3
    else:
        middle = number3
        smallest = number2
elif number2 >= number1 and number2 >= number3:
    largest = number2
    if number1 >= number3:
        middle = number1
        smallest = number3
    else:
        middle = number3
        smallest = number1
else:
    largest = number3
    if number1 >= number2:
        middle = number1
        smallest = number2 
    else:
        middle = number2
        smallest = number1  
print(smallest, middle, largest)
    