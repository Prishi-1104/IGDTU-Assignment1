#Program to count the number of each charcters in a string
a=input("Enter a string:")
dict = {}

for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)