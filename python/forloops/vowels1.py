s1= raw_input("enter a string check how many  vowels does it have")
d={"a":0,"e":0,"i":0,"o":0,"u":0}
for i in s1 :
    if i in d:
        d[i]=d[i]+1
print d
