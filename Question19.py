s=input("Please Enter String")
if not s:
    print("The string is empty.")
elif s.isupper():
    print("The string is in uppercase.")
elif s.islower():
    print("The string is in lowercase.")
else:
    print("The string is mixed case.")