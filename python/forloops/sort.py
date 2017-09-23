a=[1,2,33,23,4,5,6,8]
print a
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j] :
            a[i],a[j]=a[j],a[i]
print a
