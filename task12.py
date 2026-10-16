distance=float(input("Enter the distance in kilometers: "))
if distance < 0:
    print("Invalid distance")
else:
    startingfee = 2.0
    if distance <= 5:
        rate = 0.70
    elif distance <= 15:
        rate = 0.60
    else:
        rate = 0.50
distancefee = distance * rate
totalfare = startingfee + distancefee
print("Starting fee: ", startingfee)
print("Distance fee: ", distancefee)
print("Total fare: ", totalfare)