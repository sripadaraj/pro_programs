s1=raw_input("enter a string check how many  vowels does it have")
v={1:"a",2:"e",3:"i",4:"o",5:"u"}
V={1:"A",2:"E",3:"I",4:"O",5:"U"}
for i in s1:
    for j in range(1,6):
        if i==v[j] or i==V[j] :
            print (i)
        
