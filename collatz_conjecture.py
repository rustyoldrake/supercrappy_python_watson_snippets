# python code for Collatz conjecture
# https://en.wikipedia.org/wiki/Collatz_conjecture
# Consider the following operation on an arbitrary positive integer:
# If the number is even, divide it by two.
# If the number is odd, triple it and add one

#Collatz conjecture by julia
import os

os.system('clear')

print("---------")
print("Welcome to Collatz conjecture in Python")
print("Accepting an input - even numbers divide by 2; odd numbers triple and add 1")
j = input("What number shall I test ? " )
j = int(j)

# program sets originalBase to keep track of Starting number (for end)
originalBase = int(j)

# program creates a COUNTER to see how many times through the loop we go
counter = 0

#
while(j>1):
    counter = counter + 1 # each time through loop

    if (j % 2) == 0:
        j = j/2
        print(int(j))
    else:
        j = j*3+1
        print(int(j))

if (j==1):
    print("program complete!")
    print("Your entry of", originalBase, " has become 1!")
    print("the number of steps to solve was ",counter,"steps")
