#program that calculates the sum of digits of a number
a=int(input("Enter a  number:"))
s=0
while a>0:
    r= a%10
    s=s+r
    a=a//10
print("The sum of Digits:",s)