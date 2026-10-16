amount=float(input("Enter the amount: "))
if amount < 0:
    print("Invalid amount")
else:
    if amount <= 100:
        discount = 0.00
    elif amount <= 300:
        discount = 0.10
    elif amount <= 500:
        discount = 0.15
    else:
        discount = 0.20
    discount_amount = amount * discount
    final_price = amount - discount_amount
    print("Original price:", amount, "AZN")
    print("Discount amount:", discount_amount, "AZN")
    print("Final price:", final_price, "AZN")