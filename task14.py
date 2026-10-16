a=float(input("Enter a number: "))
b=float(input("Enter a second number: "))
c=float(input("Enter a third number: "))
if a > 0 :
    if b > 0:
        if c > 0:
            if a + b > c:
                if a + c > b:
                    if b + c > a:
                        if a==b and b==c:
                            print("Equilateral triangle")
                        elif a==b or a==c or b==c:
                            print("Isosceles triangle")
                        else:
                            print("Scalene triangle")
                    else:
                        print("Triangle cannot be created")
                else:
                    print("Triangle cannot be created")
            else:
                print("Triangle cannot be created")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")