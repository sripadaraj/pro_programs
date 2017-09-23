num=input("enter the number to convert from  decimal to octal")
sum1=''
while(num>=1):
        a=num%16
        num=num/16
        sum1=sum1+str(a)
for i in sum1[::-1]:
    if (i=='10'):
        print "A",
    elif (i=='11'):
        print 'B',
    elif (i=='12'):
        print "C",
    elif (i=='13'):
        print 'D',
    elif (i=='14'):
        print 'E',
    elif (i=='15'):
        print 'F',
    else:
        print i,
