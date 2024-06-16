#program that reada data from a csv file and prints to a console
import csv
with open('List.csv', mode ='r')as file:
  a= csv.reader(file)
  for lines in a:
        print(lines)