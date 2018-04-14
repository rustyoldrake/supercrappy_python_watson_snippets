# choose your own adventure - part 1 - the basics
import csv # this is for importing the CSV files to lists
import random
import os
import time

os.system('clear')

# Get user to tell system the number to test whether prime or not
print ("\n Hello, Welcome to CHOOSE YOUR OWN ADVENTURE \n")
print ("PART 1 - to begin we're going to make a basic story that")
print ("changes each time you run it \n ")

#N = input("Type in ANY number to begin: ")

# ANIMALS 1
with open('animals.csv', 'rb') as f:
    reader = csv.reader(f)
    animal_list_1 = list(reader)

# ADJECTIVES 2
with open('adjectives.csv', 'rb') as f:
    reader = csv.reader(f)
    adjective_list_2 = list(reader)

# VERBS 3
with open('verbs.csv', 'rb') as f:
    reader = csv.reader(f)
    verbs_list_3 = list(reader)

count = 0
while (count < 60):
    R1a = random.randint(1,random.randint(1,len(animal_list_1)))
    R1b = random.randint(1,random.randint(1,len(animal_list_1)))
    R2a = random.randint(1,random.randint(1,len(adjective_list_2)))
    R2b = random.randint(1,random.randint(1,len(adjective_list_2)))
    R3a = random.randint(1,random.randint(1,len(verbs_list_3)))
    R3b = random.randint(1,random.randint(1,len(verbs_list_3)))

    os.system('clear')

    print ("\n\n\n"),
    print (" Once upon a time there was a"),
    print (''.join(adjective_list_2[R2a])),
    print (''.join(animal_list_1[R1a])),
    print ("\n It was"),
    print (''.join(verbs_list_3[R3a])),
    print ("a"),
    print (''.join(adjective_list_2[R2b])),
    print (''.join(animal_list_1[R1b])),
    print ("\n\n")
    time.sleep(4)
