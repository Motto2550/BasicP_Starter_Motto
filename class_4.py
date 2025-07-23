customertype = str(input("Enter your membership : "))
price = int(input("Enter your food price : "))
date = int(input("Enter your date : "))

if customertype == ("G") :
    customertype = ("Gold")
    if price >= 1000 :
        discount = 15
    elif price < 1000 :
        discount = 10
elif customertype == ("S") :
    customertype = ("Silver")
    if price >= 1000 :
        discount = 10
    elif price < 1000 :
        discount = 5
else :
    customertype = ("Normal")

dprice = price * discount / 100

if date % 2 != 0 and dprice > 500:
    dprice = dprice * 5 / 100
                    
if dprice < 800 :
    shipmentp = 50
    dprice = dprice + 50
else :
    shipmentp = 0

finalprice = dprice + shipmentp

print("Membership : ",customertype)
print("After discount price : ",dprice)
print("Shipment price : ",shipmentp)
print("Finalprice price : ",finalprice)
