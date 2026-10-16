userage=int(input("Enter your age: "))
if userage >= 0 and userage <=12:
    print("Child")
elif userage >= 13 and userage <=17:
    print("Teenager")
elif userage >= 18 and userage <=64:
    print("Adult")
elif userage >= 65:
    print("Senior")
else:
    print("Invalid age")