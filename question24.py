# program that acts as a simple calculator
a= input("Enter the calculation you want to perform:('+','-','*','/'):")
if a=='+':
    x= int(input("Enter a number:"))
    y= int(input("Enter another number:"))
    print("The Sum is:",(x+y))
elif a=='-':
    p= int(input("Enter a number:"))
    q= int(input("Enter another number:"))
    if(p>q):
        print("The difference is:",p-q)
    else:
        print("The Difference is:",q-p)

elif a=='*':
    e= int(input("Enter a number:"))
    f= int(input("Enter another number:"))
    print("The Product is:",e*f)

elif a=='/':
    c= int(input("Enter a number:"))
    d= int(input("Enter another number:"))
    print("The division is:",c//d)

else:
    print("Invalid Input")