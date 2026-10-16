score=int(input("Enter your score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 91:
    print("Grade: A")
elif score >= 81:
    print("Grade: B")
elif score >= 71:
    print("Grade: C")
elif score >= 61:
    print("Grade: D")
elif score >= 51:
    print("Grade: E")
else:
    print("Grade: F")
