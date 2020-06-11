# frequency_bin_display.py


from time import sleep


print ("64 Bins across 0Hz - 24khz = 375 Hz per step ")
#print ("---------- ---------- ---------- ---------- ---------- ---------- ----")

for i in range(64):



    for b in range(64):
        if (b==i):
            print(1, end = '')
        else:
            print(0, end = '')

    print (" - Test", i)
    sleep(0.05)    #in seconds
