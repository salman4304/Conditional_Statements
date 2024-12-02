first_number=float(input("Enter First Number"))
second_number=float(input("Enter Second Number"))
operator=input("Please Enter Operator +,*,-,/")
if operator == "+":
   add=first_number+second_number
   print(add)
elif operator == "-":
   sub=first_number-second_number
   print(sub)
elif operator == "*":
   mul=first_number*second_number
   print(mul)
elif operator== "/":
   if second_number!=0:
     div=first_number/second_number
     print(div)
   else:
      print("Division is invalid")
else:
   print("Invalid Entry")