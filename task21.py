storedpin="0427"
pin=input()
if len (pin) == 0 :
    print("PIN is required")
elif len (pin) != 4 :
    print("PIN must have 4 digits")
elif not pin.isdecimal() or not pin.isascii():
    print("Digits only")
elif pin==storedpin:
    print("Access granted")
else:
    print("PIN is incorrect")