print "a program to take input from user a number and check if it isprime number or not"
count=0
for i in range(2,50):
    for w in range(1,i):
        if i%w==0 :
            count=count+1
    if count<2:
        print i,
    count=0
    
