a=raw_input("enter the string")
d= {}
    for n in a:
         if n in d:
            d = d[n] + 1
         else:
            d[n]= 1
        

