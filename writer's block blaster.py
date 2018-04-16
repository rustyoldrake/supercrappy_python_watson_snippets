# WRITER'S BLOCK BLASTER
import csv # this is for importing the CSV files to lists
import random # this is to generate random number
import os # reseting the screen
import time # this lets system wait for a few seconds - delay

# os.system('clear')


print ("\n Hello, Welcome to WRITER'S BLOCK BLASTER \n")
print ("PART 1 - to begin we're going to generate idea seeds that")
print ("randomly pulls CSV data - changes each loop \n ")
print ("YOU WILL BE ASSIGNED AN IDEA TO WRITE ABOUT!\n ")

# os.system('say OK!  bye bye Writers Block.  Time to get creative!')


# IMPORT ANIMALS 1
with open('animals.csv', 'rb') as f1:
    reader = csv.reader(f1)
    animal_list_1 = list(reader)

# IMPORT ADJECTIVES 2
with open('adjectives.csv', 'rb') as f2:
    reader = csv.reader(f2)
    adjective_list_2 = list(reader)

# IMPORT VERBS 3
with open('verbs.csv', 'rb') as f3:
    reader = csv.reader(f3)
    verbs_list_3 = list(reader)

# IMPORT EMOTIONS 4
with open('emotions.csv', 'rb') as f4:
    reader = csv.reader(f4)
    emotions_list_4 = list(reader)

# Debugging and demo section for learning - Test
# print (animal_list_1[4])
# print (adjective_list_2[69])
# print (verbs_list_3[9])
print (emotions_list_4[44])

# LET"S GO!
ideas = input("How many ideas should I test? (e.g. 10-1000) ")
delay = 0.01

count = 0
while (count < ideas):
    R1a = random.randint(1,random.randint(1,len(animal_list_1)-1))
    R1b = random.randint(1,random.randint(1,len(animal_list_1)-1))
    R1c = random.randint(1,random.randint(1,len(animal_list_1)-1))
    R2a = random.randint(1,random.randint(1,len(adjective_list_2)-1))
    R2b = random.randint(1,random.randint(1,len(adjective_list_2)-1))
    R3a = random.randint(1,random.randint(1,len(verbs_list_3)-1))
    R3b = random.randint(1,random.randint(1,len(verbs_list_3)-1))
    R4a = random.randint(1,random.randint(1,len(emotions_list_4)-1))
    R4b = random.randint(1,random.randint(1,len(emotions_list_4)-1))

    os.system('clear')

    print ("\n\n\n"),
    print ("  Once upon a time there was a"),
    print (''.join(adjective_list_2[R2a])),
    print (''.join(animal_list_1[R1a])),
    print (" feeling"),
    print (''.join(emotions_list_4[R4a])),
    print ("\n  It was"),
    print (''.join(verbs_list_3[R3a])),
    print ("a"),
    print (''.join(adjective_list_2[R2b])),
    print (''.join(animal_list_1[R1b])),
    print (" that felt \n "),
    print (''.join(emotions_list_4[R4b])),
    print (" about a nearby"),
    print (''.join(animal_list_1[R1c])),
    print ("\n\n")
    time.sleep(delay)
    count = count + 1

print (" \n FOUND! the best story for you!")
print (" \n Your Assignment: Write a story or poem about this IDEA!")
print (" \n ")

# os.system('say Your Assignment: Write a story or poem about this IDEA.')
