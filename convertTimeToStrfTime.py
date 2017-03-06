#!/usr/bin/env python

"""
Given that input_time actually represents
an integer value in seconds since the epoch - and has the
value 0 at precisely "Thu Jan 1 00:00:00 1970", 
write a better implementation of this function.
"""

import time

def normalize(input_time):
    t=time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(input_time))
    print t
           
def main():
    j = normalize(0)
    v = normalize(1284101485)

if __name__ == "__main__":
    main()

"""
$ ./convertTimeToStrfTime.py 
Wed Dec 31 16:00:00 1969
Thu Sep 09 23:51:25 2010


"""
