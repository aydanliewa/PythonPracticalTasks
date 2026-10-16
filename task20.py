studentID=input()
if len(studentID)==0:
    print("Invalid: Empty input")
elif not studentID.isascii():
    print("Invalid: Non-ASCII characters")
elif not studentID.isdecimal():
    print("Invalid: Non-digit characters")
elif len(studentID) != 8 :
    print("Invalid: Exactly 8 digits")
else:
    print("STUDENT ID ACCEPTED")