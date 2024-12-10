import math
a=int(input("enter the 1st value : "))
b=int(input("enter the 2nd value : "))
c=int(input("enter the 3rd value : "))
d=(b*b)-(4*a*c)
if(d>0):
    X1=(-d+math.sqrt(d))/(2*a)
    X2=(-d+math.sqrt(d))/(2*a)
    print("the roots are :" ,X1,X2)
elif(d==0):
    x=(-b)*(2*a)
    print("The root is : ",x)
else:
    print("The roots are imaginary")
    
    