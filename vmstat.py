#!/usr/bin/env python

"""


"""
import os
import sys
import itertools

def vmstat(path):
    fileobj = open(path,'r')
    fileReader = fileobj.readlines() 
    #print fileReader
    fileobj.close()
    
    myNelements = fileReader
    topNlines= itertools.islice(myNelements,4) 
    for i in topNlines:
        print i

def main():
    myList=sys.argv
    path_of_file = myList[1]
    v = vmstat(path_of_file)
    #Number_of_lines = myList[2]
    #v = vmstat(path_of_file,Number_of_lines)


if __name__ == "__main__":
    main()


"""
$ ./vmstat.py '/proc/meminfo' 
MemTotal:        1024412 kB

MemFree:           82524 kB

MemAvailable:     366380 kB

Buffers:           69532 kB

"""
