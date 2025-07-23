score = int(input("Enter your score : "))

if score >= 50 :
    print("PASS !!!")
    if score < 60 :
        grade = ("D")
    elif score >= 60 and score < 70 :
        grade = ("B")
    elif score >= 70 and score < 80 :
        grade = ("C")
    elif score >= 80 :
        grade = ("A")
    print("Grade : ",grade)
else :
    print("Fail !!!")
    print("Grade F")
