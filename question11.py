#Fibonacci Sequence
n = int(input("Enter a number:"))
a = 0
b = 1
print(a)
print(b)
c = b 
count = 1
 
while count <= n:
    print(c)
    count += 1
    a, b = b,c
    c = a + b
print()