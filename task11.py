usage=float(input("Enter the usage in kWh: "))
if usage < 0:
    print("Invalid usage")
else:
    if usage>=0 and usage<=100:
        bill = usage * 0.08
    elif usage>100 and usage<=300:
        bill = usage * 0.12
    else:
        bill = usage * 0.15
    
print("Usage: ", usage, "kWh")
print("Total bill:", bill, "AZN")
print("Applied rate:", bill/usage, "AZN per kWh")