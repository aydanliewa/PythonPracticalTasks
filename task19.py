drinkcode=input()
quantity=int(input())
if quantity < 1 or quantity > 10 :
    print("Invalid quantity")
else:
    match drinkcode:
        case "T":
            price=2
            drink="Tea"
        case "C":
            price=4
            drink="Coffee"
        case "J":
            price=3
            drink="Juice"
        case _:
            price=0
            drink="Not found"
    if drink=="Not found":
        print("Invalid drinkcode")
    else:
        total=quantity*price
        status="Large order" if total >=20 else "Regular order"
        print("Drink", drink)
        print("Quantity", quantity)
        print("total", total, "AZN")
        print("Status:", status)