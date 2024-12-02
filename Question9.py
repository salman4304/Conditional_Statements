first_side=int(input("Please Enter First Side of Triangle"))
second_side=int(input("Please Enter Second Side of Triangle"))
third_side=int(input("Please Enter Third Side of Triangle"))
if first_side > 0 and second_side > 0 and third_side > 0:
    if first_side + second_side > third_side:
        if first_side + third_side > second_side:
            if second_side + third_side > first_side:
                print("Triangle is valid")
            else:
                print("Triangle is invalid")
        else:
            print("Triangle is invalid")
    else:
        print("Triangle is invalid")
else:
    print("Invalid Triangle")
