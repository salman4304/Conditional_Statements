year=int(input("Please Enter Year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Entered Year is Leap Year")
        else:
            print("Entered Year is not Leap Year")

    else:
        print("Entered Year is not Leap Year")
else:
    print("Entered Year is not Leap Year")