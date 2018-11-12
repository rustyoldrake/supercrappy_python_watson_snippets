# math_gods.py
import random
import time
import os

print("This is a program to make you a math god \n ")

for i in range(0,5):
   #print("problem number", i)

   x = random.randrange(1, 13) # First random number to multiply
   y = random.randrange(1, 13) # Second random number to multiply

   os.system('cls' if os.name == 'nt' else 'clear') # Clear Screen
   print(" \n ")
   print(" ", x, " X ", y, "=")

   speech = "say %s times %s" % (x,y)
   os.system(speech)

   time.sleep(5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(" \n ")
   print(" ", x, " X ", y, "=",(x*y))

   speech = "say %s times %s equals %s" % (x,y,(x*y))
   os.system(speech)

   time.sleep(2)
