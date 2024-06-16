#program that removes all the punctuation from a string
a=input("Enter a string:")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in a:
    if i in punc:
        a= a.replace(i,"")

print(a)