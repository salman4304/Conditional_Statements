num=float(input("Enter Number"))
lower=float(input("Enter Lower Limit"))
upper=float(input("Enter Higher Limit"))
if num > lower and num < upper:
    print("Entered number {num} is in range")
else:
    print("Entered number {num} is not in range")