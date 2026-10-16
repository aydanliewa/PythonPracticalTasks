examscore=int(input("Enter your exam score: "))
schoolscore=int(input("Enter your school score: "))
age=int(input("Enter your age: "))
if examscore < 0 or examscore > 700 or schoolscore < 0 or schoolscore > 100 or age < 0:
    print("Invalid input")
else:
    if age < 16:
        print("Rejected: Age below 16") 
    elif examscore >= 600 and examscore <= 700:
        print("Approved: Scholarship granted")
    elif examscore >= 450 and examscore < 600:
        print("Approved")
    elif examscore >= 300 and examscore < 450:
        if schoolscore >= 80:
            print("Approved")
        else:
            print("Rejected: School score below 80")

    elif examscore < 300:
        print("Rejected: Exam score below 300")
    