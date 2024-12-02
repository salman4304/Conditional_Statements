first_number=int(input("Please Enter First Number"))
second_number=int(input("Please Enter Second Number"))
third_number=int(input("Please Enter Third Number"))
if first_number > second_number and first_number > third_number:
    print("First Number is Largest")
elif second_number > first_number and second_number > third_number:
    print("Second Number is Largest")
else:
    print("Third Number is Largest")