# Variable_CPU_load.py
# This program is a simple counter loop for deployment on
# Edge devices - like RaspberryPI - that compels the CPU to work
# harder (counting, looping) over a period of time - generating varying load and heat

# Upon initialization - the beat period is set - (quasi random duty cycle)
# if deployed on a stack of 4 raspberry PIs, they should each be running unique load duty cycles
# if co-located , may see some temperature variation based on radiated heat from neighbour

import random # for the rando range
import time # for the waity wait

index = 0 # our counter for our looping
max = random.randint(10,40)*1000000 # 10 t0 40 million

###  Beat periood

print("initializing system")
rando_calrissian = random.randint(5,15)*60 # Wait time in seconds (range) (5,6,7.. to 15 minutes, in seconds period)
## REMEMBER! The total period will be rando_calrissian PLUS the time to count (e.g. might be 5.8 minutes - )

print (rando_calrissian," seconds between repeats") # can also log this expliticly

print (max," loop length") # Big number - e.g. 1 million takes about 4 seconds on a mac - slower on pi


while True:
    print("I'm waiting for rando_calrissian to expire in ",rando_calrissian," seconds")
    time.sleep(rando_calrissian) # Delay for 1 minute (60 seconds).

    ### Loopy count-stein
    for index in range(1,max):
        print (index)
