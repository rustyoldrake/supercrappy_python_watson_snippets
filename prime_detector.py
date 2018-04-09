# PRIME DETECTOR PROGRAM - by Lucy
# Program to let user input a number , and tell them if it is PRIME
# Prime numbers are evenly divisible only by themselves and 1 - non-prime have other factors
# Youtube of code being tested here: https://youtu.be/DGv89M9fqbc
# TIME - takes 2 seconds to test 10 million; 13 seconds for 100m and 125 seconds for 1 billion on a mac

# Get to know the user's name
print("This code will test if a number is prime. Let's get started!")
userName = raw_input("What is your name? ")

# Get user to tell system the number to test whether prime or not
print ("Hello, " + userName)
testNumber = input(userName + ", what number do you want to test? ")


## Let's time how long it takes
from datetime import datetime
startTime = datetime.now()
print datetime.now() - startTime

#N = testNumber - 1  # TO begin - Start Index at one LESS than test number (e.g. 103 starts at 102)

# Changed this to TN/2 - as you'll never have an neat factor more than half of number
N = testNumber/2  # TO begin - Start Index at one LESS than test number (e.g. 103 starts at 102)

S = 0 # THIS IS THe bucket for adding our factors.  If it stays 0, then no factors other than TN and 1, therefore meets definition of prime

while N > 1: # Main loop to run "testNumber-times less two" loops - e.g. testing 100 loops from 99 down to 2, then stops (so 98 times
    if(testNumber%N == 0 ): # if TN/N yields a ZERO remainder (cause % is the remainder part after division operation) then we know the number is evenly divisible by N - e.g. 100%50 is 2 remainer 0 so true.
        print(N)
        S = (S + N)
    N = N - 1 # last thing we do in the loop is take one off N, and do again!

if(S == 0):
    print("Your number is Prime, " + userName + "!")
else:
    print("Your number is NOT prime, " + userName + ", your factors are above!")

print("time to complete")
print datetime.now() - startTime
