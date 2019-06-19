# The MIT License (MIT)
# Source https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
# Vladimir Ignatev

# Goofing around with program to demonstrate "time passing" at command line... nice little program from Vladimir plus wrapper from comments

import sys
import time

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)


total = 100
i = 0
while i < total:
    progress(i, total, status='Doing somewhat long job')
    time.sleep(0.5)  # emulating long-playing job
    i += 1
