productcode=input()
quantity=input()
couponcode=input()
deliverycode=input()
match productcode:
    case "K":
        price=40
        productname="Keyboard"
    case "M":
        price=20
        productname="Mouse"
    case "H":
        price=60
        productname="Headphones"
    case _:
        productname="Invalid"
if productname=="Invalid":
    print("Invalid product code")
elif len(quantity)==0 or not quantity.isascii() or not quantity.isdecimal():
    print("Invalid quantity format")
else:
    quantity=int(quantity)
    if quantity < 1 or quantity > 5:
        print("Quantity must be between 1 and 5")
    elif couponcode!="NONE" or couponcode!="SAVE10":
        print("Ïnvalid coupon code")
    else:
        total=quantity*price
        discount=0.0
        if couponcode=="SAVE10":
            if total>=100:
                discount=total*0.10
            else:
                print("Coupon is ineligible")
        newtotal=total-discount
        match deliverycode:
            case "Pickup(free)":
                deliveryfee=0.0
            case "Standart":
                deliveryfee=0 if newtotal>=80 else 5.0
            case _:
                deliveryfee=1
        if deliveryfee==1:
            print("Invalid delivery code")
        else:
            finaltotal=newtotal+deliveryfee
            print("Product:", productname)
            print("Quantity:", quantity)
            print("Subtotal:", newtotal, "AZN")
            print("Discount:", discount, "AZN")
            print("Delivery fee:", deliveryfee, "AZN")
            print("Final total:", finaltotal, "AZN")
            
