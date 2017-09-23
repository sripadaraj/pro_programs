#def char_frequency(str1):
str1=raw_input("enter the string")
dict1 = {}
for n in str1:
    if n in dict1:
        dict1[n] += 1
    else:
        dict1[n] = 1
print dict1
#print(char_frequency('google.com'))
