monstername = ("Nigaboss")
monsterhp = 300
sword = ("Sword")
sworddm = 50
bow = ("Bow")
bowdm = 40
staff = ("Staff")
staffdm = 30
roundplus = 0

print("Menu type 1 to fight type 2 to run")
menu = int(input("Enetr your choice : "))

if menu == 1 :
    print("Name :",monstername,"Hp :",monsterhp)
    round = int(input("Enter number of round U want to play : "))
    for i in range (round) :
        if roundplus == round :
            print("You died because the round is over")
            break
        elif monsterhp == 0 :
            print("You win !!!")
            break
        elif monsterhp <= 0 :
            monsterhp = 300
            print("Nigaboss is reincarnated !!!")
            print("Name :",monstername," Hp :",monsterhp)

        weapon = str(input("Choose your weapon Bow,Staff,Sword : "))
        if weapon == ("Sword") and monsterhp > 0:
            monsterhp = monsterhp-sworddm
            print("Name :",monstername," Hp :",monsterhp)
            roundplus = roundplus + 1
        elif weapon == ("Bow") and monsterhp > 0:
            monsterhp = monsterhp-bowdm
            print("Name :",monstername," Hp :",monsterhp)
            roundplus = roundplus + 1
        elif weapon == ("Staff") and monsterhp > 0:
            monsterhp = monsterhp-staffdm
            print("Name :",monstername," Hp :",monsterhp)
            roundplus = roundplus + 1

elif menu == 2 :
    print("You died because Nigaboss is too fast.")
else :
    print("???")