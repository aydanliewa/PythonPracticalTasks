phonenumber=input()
prefix=phonenumber[:3]
if len(phonenumber)==0:
    print("Invalid: Empty input")
elif not phonenumber.isdecimal() or not phonenumber.isascii():
    print("Invalid: Digits only")
elif len(phonenumber)!=10 or not phonenumber.startswith("0"):
    print("Invalid: Incorrect format")
else:
    match prefix:
        case "050":
            print("Accepted")
        case "051":
            print("Accepted")
        case "055":
            print("Accepted")
        case "077":
            print("Accepted")
        case "070":
            print("Accepted")
        case "099":
            print("Accepted")
        case _:
            print("Invalid prefix")