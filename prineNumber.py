#for i in range(1,101):
    #if i %7==0:
   #  print(i)

for n in range(1,101):
    count=0
    for i in range(2,(n//2+1)):
        if(n%1==0):
         count=count+1
         break
    if(n!=1 and count==0):
        print("%d"%n,end='')