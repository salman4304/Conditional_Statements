first_side=int(input("Enter First Side"))
second_side=int(input("Enter Second Side"))
third_side=int(input("Enter Third Side"))
#Equilateral Triangle:
if first_side==second_side and second_side==third_side:
     print("Triangle is Equilateral")
elif first_side!=second_side and second_side!=third_side and first_side!=third_side:
  print("Triangle is Scalene")
else:
  print("Triangle is Isosceles")