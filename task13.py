userage=int(input("Enter your age: "))
monthlysalary=float(input("Enter your monthly salary: "))
loan=float(input("Enter the loan amount: "))
if userage < 0 or monthlysalary < 0 or loan <= 0:
    print("Invalid input")
else:
    if userage < 18:
        print("Rejected: Age below 18")
    else:
        if monthlysalary < 500:
            print("Rejected: Salary below 500 AZN")
        else:
            if loan > monthlysalary * 10:
                print("Rejected: Requested loan above 10 times monthly salary")
            else:
                print("Approved: Loan granted")