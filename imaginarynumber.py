import math
a=int(input("enter the 1st value : "))
b=int(input("enter the 2nd value : "))
c=int(input("enter the 3rd value : "))

if((a+b)>c and (a+c)>b and (c+b)>a):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("the area is : %0.2f"%area)
else:
    print("Triangle is not possible")