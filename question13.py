#program that asks user for their birth year and calculates the age
a=int(input("Enter your birth year:"))
b= int(input("Enter the current year:"))
i=0
for a in range(a,b):
    i=i+1
print("Your age is:",i)