count=0
for i in range(2,50):
    for w in range(1,i):
        if(i%w==0):
            count=count+1
    if count<2 :
        print i,"is prime"
    count=0
    

        
