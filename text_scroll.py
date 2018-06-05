# Simple Text Scroll in Python

import csv # this is for importing the CSV files to lists
import random # this is to generate random number
import os # reseting the screen
import time # this lets system wait for a few seconds - delay

os.system('clear')


while(1):
    for x in xrange(0, 9):
        print '%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d ' % (x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)
        time.sleep(.05)
        for y in xrange(9, 0, -1):
            print '%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d  ' % (y,y,y,y,y,y,y,y,y,y,y,y,y,y,y,y,y,y)
            time.sleep(.05)
