i=input("enter the number to check if its a prime or not")
c=0
for v in range (1,i):
    if i%v==0:
        c=c+1
if c<2:
    print " the number",i,"is prime"
else :
    print "it is not prime"
