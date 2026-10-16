studentID=input()
age=input()
workshop=input()
payment=input()
if len(studentID)!=8 or not studentID.isdecimal() or not studentID.isascii():
    print("Invalid student ID")
elif len(age)==0 or not age.isdecimal() or not age.isascii():
    print("Invalid age format")
else:
    age=int(age)
    if age < 16 or age > 65 :
        print("Age is out of range")
    else:
        match workshop:
            case "PY":
                workshopname="Python Basics"
                fee=30.0
                minage=16
            case "WEB":
                workshop="Web Development"
                fee=40.0
                minage=16
            case "CY":
                workshopname="Cybersecurity"
                fee=50.0
                minage=18
            case _:
                workshopname="Invalid"
        if workshopname=="Invalid":
            print("Invalid workshop code")
        elif age < minage:
            print("Age is not suitable for requirement")
        else:
            discount=fee*0.20 if (16<=age<=18) else 0.0
            finalfee=fee-discount
            if len(payment)==0 or not payment.isdecimal() or not payment.isascii():
                print("Ïnvalid payment format")
            else:
                payment=int(payment)
                if payment<finalfee:
                    missingamount=finalfee-payment
                    print("Insufficient payment","Missing amount", missingamount, "AZN")
                else:
                    change=payment-finalfee
                    print("Registration confirmed")
                    print("Student ID:", studentID)
                    print("Workshop:", workshopname)
                    print("Discount:", discount, "AZN")
                    print("Final fee:", finalfee, "AZN")
                    print("Change:", change, "AZN")


