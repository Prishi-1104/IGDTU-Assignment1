#a program that copies the contents of one text file to another
a=open("abc.txt",'r')
b=open("def.txt",'w')
for i in a:
    b.write(i)