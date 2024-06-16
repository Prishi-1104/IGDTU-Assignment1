#a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
a= input("Enter the conversion method: 'F' for Celcius to Fahrenheit and 'C' for Fahrenheit to Celcius")
if a== 'F':
    x=int(input("Enter the number:"))
    print("The converted value is:",((9//5)*x)+32)
elif a=='C':
    y=int(input("Enter the number: "))
    print("The converted value is:",((y-32)*5)//9)
else:
    print("Invalid Input")