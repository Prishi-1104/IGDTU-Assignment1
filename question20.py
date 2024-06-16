#program to take a list of numbers and return their sum
total = 0
l= [11, 5, 17, 18, 23]
for i in range(0, len(l)):
    total = total + l[i]
print("Sum of all elements in given list: ", total)
