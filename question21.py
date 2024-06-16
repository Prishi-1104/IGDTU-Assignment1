# program that counts the occurrences of a specific element 
from collections import Counter
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
a= 9
b= Counter(l)
print(b[a])

