score=int(input("Enter your score: "))
if score > 100 or score < 0:
    print("Invalid score")
else:
    result="Pass" if score >= 51 else "Fail"
    print(result)

