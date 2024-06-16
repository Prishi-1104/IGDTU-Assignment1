#program that check if two strings are anagrams are each other
a=input("Enter a string:")
b= input("Enter another string:")
if( sorted(a)== sorted(b)):
    print("They are anagrams")
else:
    print("They are not anagrams")
