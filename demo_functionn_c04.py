def grade(score) :
    if score >= 50 :
        print("you passed !!!")
        if score >= 80 :
            print("Grade A")
        elif score >= 70 :
            print("Grade B")
        elif score >= 60 :
            print("Grade C")
        else :
            print("Grade D")
    else :
        print("you failed !!!")

grade(70)
