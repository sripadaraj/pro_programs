num=input("enter the number to convert from  decimal to octal")
sum1=""
while(num>=1):
        a=num%8
        num=num/8
        sum1=sum1+str(a)
print sum1[::-1]
