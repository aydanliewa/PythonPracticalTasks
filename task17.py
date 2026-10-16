member=input()
total=float(input())
if total < 0 or (member != "yes" and member != "no"):
    print("Invalid input")  
else:
    fee=0 if (total >=50 or member == "yes") else 5
    finaltotal= total + fee
    print("Final total: ", finaltotal)
    print("Fee: ", fee)