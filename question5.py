#program that takes a string input and wites it to text file
a= input("Enter the data:")
with open("abc.txt",'w') as file:
    file.write(a)