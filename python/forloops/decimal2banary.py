num=input("enter the number to convert from decimal to binary")
sum1=""
div=1
while(num>=1):
        a=num%2
        num=num/2
        sum1=sum1+str(a)
print sum1[::-1]
