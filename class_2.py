distance = int(input("Enter distance : "))
vat = 0.07

if distance < 5 :
    print("FREE!!!")
    vatprice = 0 * vat 
    finalprice = 0 + vatprice
elif distance >= 5 and distance <= 50 :
    print("10 BAHT")
    vatprice = 10 * vat 
    finalprice = 10 + vatprice
elif distance > 50 and distance <= 100 :
    print("15 BAHT")
    vatprice = 15 * vat 
    finalprice = 15 + vatprice
elif distance > 100 and distance <= 300 :
    print("25 BAHT")
    vatprice = 25 * vat 
    finalprice = 25 + vatprice
elif distance > 300 and distance <= 500 :
    print("35 BAHT")
    vatprice = 35 * vat 
    finalprice = 35 + vatprice
else :
    print("45 BAHT")
    vatprice = 45 * vat 
    finalprice = 45 + vatprice

print("Vat : " ,vatprice)
print(finalprice, "BAHT")