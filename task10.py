balance=1000.0
amount=float(input("Enter the amount to withdraw: "))
if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
     balance=balance-amount
     print("Withdrawal successful")
     print("Remaining balance:", balance)