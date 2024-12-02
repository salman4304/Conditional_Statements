num=int(input("Please Enter Number"))
if num>1:
    for x in range(2,num):
        if num%x==0:
            print(f"Entered Number {num} is not Prime Number")
            break
    else:
       print(f"Entered Number {num} is Prime Number")
else:
 print(f"Entered Number {num} is not Prime Number")