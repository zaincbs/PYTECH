#!/usr/bin/env python

"""


"""
import os
import sys
import itertools

def vmstat():
    myList=[]    
    newList=[]
    saveDataList=[]

    fileobj = open('/proc/meminfo','r')
    fileReader = fileobj.readlines() 
    #print fileReader
    fileobj.close()
    #reading /proc/meminfo file
    
    #now printing first 4 elements of vmstat
    myNelements = fileReader
    topNlines= itertools.islice(myNelements,4) 
    #print topNlines
    	
    #converting topNlines to a list, since itertools.islice return
    #an object
    myList= list(topNlines)
    #print myList
    
    #removing spaces from list elements and creating a newList so that
    #it is converted further into tokens
    for i in myList:
        i = i.split()
        newList.append(i)
    """
    newList = [['MemTotal:', '1017564', 'kB'], ['MemFree:', '108396', 'kB'], ['Buffers:', '58764', 'kB'], ['Cached:', '219060', 'kB']]
    """
    #calculations of memmory: free_cached, free_unused, used
    memTotal = newList[0][1]
    free_cached = int(newList[2][1] + newList[3][1])
    free_unused = int(newList[1][1])
    used = int(newList[0][1]) - free_cached - free_cached

    saveDataList.append(['system.mem.free_cached ',' ', free_cached , ' ',memTotal])
    saveDataList.append(['system.mem.free_unused ' ,newList[0][1], ' ',memTotal ])
    saveDataList.append(['system.mem.used  ', used, ' ' ,memTotal ])
    #print saveDataList
    #print ""

    #for data_stored in range(0, len(saveDataList)-1):
    #    print saveDataList[data_stored]

    print 'system.mem.free_cached ',' ', free_cached , ' ',memTotal
    print 'system.mem.free_unused ' ,newList[0][1], ' ',memTotal
    print 'system.mem.used  ', used, ' ' ,memTotal

"""
$ ./vmstat.py
system.mem.free_cached    62756208932   1017564
system.mem.free_unused  1017564   1017564
system.mem.used   -125511400300   1017564 

"""

def main():
    v = vmstat()
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
