# Ryan's War Games Program

import os  # to talk to system os in mac
import sys,time,random # for the slow type

typing_speed = 150 # wpm

# function for slow type
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

## Main Program
os.system("clear")

print("_______________________________________\n")


slow_type("Greetings Professor Falkan! \n\n")
os.system("say Greetings Professor Falcon")

slow_type("Shall we play a game? \n\n")
os.system("say Shall we play a game?")


## MENU
choice ='0'
while choice =='0':
    print("----------------------")
    print("1 - TIC-TAC-TOE")
    print("2 - POKER")
    print("3 - CHESS")
    print("4 - GLOBAL THERMONUCLEAR WAR")
    print("5 - EXIT")
    print("----------------------")

    choice = input ("Please make a choice: ")

    if choice == "5":
        #print("Go to another menu")
        slow_type("goodbye \n")
    elif choice == "4":
        slow_type("4 - GLOBAL THERMONUCLEAR WAR \n")
        os.system("say GLOBAL THERMONUCLEAR WAR")
    elif choice == "3":
        slow_type("3 - CHESS \n")
    elif choice == "2":
        slow_type("2 - POKER \n")
    elif choice == "1":
        slow_type("1 - TIC-TAC-TOE \n")
    else:
        slow_type("I don't understand your choice. \n")

print("_______________________________________\n")
