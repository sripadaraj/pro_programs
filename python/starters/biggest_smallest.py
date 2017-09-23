print "The program to print smallest and biggest among three numbers"
print "_____________________________________________________________"
a=input("enter  the first number")
b=input("enter  the second number")
c=input("enter  the third number")
d=input("enter the fourth number")
if a==b==c==d : 
    print "all are equal "
else :
    if a>=b and a>=c and a>=d:
        big=a 
    if a<=b and a<=c and a<=d:
        small=a
    if b>=a and b>=c and b>=d:
        big=b
    if b<=a and b<=c and b<=d:
        small=b
    if c>=a and c>=b and c>=d:
        big=c
    if c<=a and c<=b and c<=d:
        small=c
    if d>=a and d>=b and d>=c:
        big=d
    if d<=a and d<=b and d<=c:
        small=d
    print "_______________________________________________________________"
    print "the biggest among ",a,",",b,",",c,",",d,"is :\n"
    print big
    print "the smallest among ",a,",",b,",",c,",",d,"is :\n"
    print "smallest",small
    print "_______________________________________________________________"
