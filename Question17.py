num=int(input("Please Enter Number"))
if num%2 ==0 and num%3 ==0:
    print("Number is Divisible by both 2 & 3")
elif num%2 ==0:
    print("Number is Divisible by 2 only")
elif num%3 ==0:
    print("Number is Divisible by 3 only")
else:
    print("Number is neither divisible by 2 nor by 3")