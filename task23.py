balance=1000.0
storedpin="0427"
pin=input()
amount=input()
if len(pin)!=4 or not pin.isascii() or not pin.isdecimal:
    print("Invalid PIN format")
elif pin!=storedpin:
    print("Incorrect PIN")
elif len(amount)==0 or not amount.isdecimal() or not amount.isascii():
    print("Invalid amount format")
else:
    amount=int(amount)
    if amount<10 or amount>500:
        print("Amount must be between 10 and 500 AZN")
    elif amount%10!=0:
        print("Amount must be divisible by 10")
    else:
        fee=0 if amount<=200 else 2
        newamount=amount=fee
        if newamount>balance:
            print("Ïnsufficient balance")
        else:
            balance=balance-newamount
            print("Withdrawal amount", amount, "AZN")
            print("Fee", fee, "AZN")
            print("New balance", balance, "AZN")
            