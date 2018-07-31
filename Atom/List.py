#imports the ability to get a random number
from random import *

#Create the list of words you want to chose from
alist = ["Sonic","Shadow", "Silver", "Blaze", "Charmy", "Vector", "Sally", "Espio", "Tails", "Amy", ""]

#Generates a random integer



response input ("Would you like a fun name? (Y/N?)")
while response != "N":
    if response == "Y":
        aRandomIndex == randint(0, len(aList)-1)
    print(aList[aRandomIndex])
else:
    print("{} is an invalid input." .format(response))
    response = input ("Would you like a fun name? (Y/N?)")
