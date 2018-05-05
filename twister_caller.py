# WRITER'S BLOCK BLASTER
import csv # this is for importing the CSV files to lists
import random # this is to generate random number
import os # reseting the screen
import time # this lets system wait for a few seconds - delay

from os import system

os.system('clear')
 
print ("\n Hello, Welcome to  TWISTER CALLER \n")
print ("This program will call a new twister hand every T Seconds for N Players \n")

os.system('say Welcome! How many people are playing Twister? ')
N = input("Welcome! How many people are playing Twister? ")

#os.system('How much time between turns?')
os.system('say and How long between turns? ')
T = input("How much time between turns? (seconds) ")

# list of colors and list of limbs (0,1,2,3)
limbs = ["left hand", "right hand", "left foot", "right foot"]
colors = ["red", "yellow", "green", "blue"]

## print random.randint(0,3) # how to do random number

n=1 # start with player 1

while (1):

    ### THIS PART FOR PLAYER
    speech = "say player %s" % (n)
    print("player",n)
    os.system(speech)

    if(n<N): # increase to next player, unless max players, then reset to 1
        n=n+1
    else:
        n=1

    ### THIS PART FOR COLOR AND LIMB
    l = limbs[random.randint(0,3)]
    c = colors[random.randint(0,3)]
    print(l,c)
    speech = "say %s %s" % (l,c)
    os.system(speech)

    time.sleep(T)
