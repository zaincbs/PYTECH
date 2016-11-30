#!/usr/bin/env python
"""
PYTHON FILE READER

"""
import sys
import shlex
import collections 


newdict={}
mydict={}

def add(d, keys, value):
    update= d.get(keys,[])
    update.append(value)
    d[keys] =update

def FileReaderFromDir(file1):
    countInvalid = 0
    lines = ""
    fileobj= open(file1, 'r')    
    fileReader= fileobj.readlines()

    for line in fileReader:
        if 'invalid' in line:
            countInvalid = countInvalid + line.count('invalid')
        v = shlex.split(line)
       	add(newdict,int(v[0]),v[3])
    fileobj.close()

    mydict = {k:v for k,v in newdict.iteritems() if k > 0 and not any("invalid" in s for s in v)}
    #print mydict

    print "The number of invalid lines are", countInvalid 

    IDs= raw_input("Please enter your ID/s:(enter comma separated IDs if more than one):").split(',')
    #print IDs

    for i in IDs:
        if int(i) not in mydict:
            print i,"This ID does not exist !"
        elif len(mydict[int(i)]) > 1:
            for x in mydict[int(i)]:
                print i,x
        else:
            print i,mydict[int(i)][0]
            
def main():
    myList=sys.argv
    txtfile = myList[1]
    v = FileReaderFromDir(txtfile)
if __name__ == "__main__":
    main()



"""
#Output
$ ./PythonFileReader-new.py file
The number of invalid lines are 3
Please enter your ID/s:(enter comma separated IDs if more than one):9,8
9 Value2
8 Value
8 Value
8 Value2

$ ./PythonFileReader-new.py file
The number of invalid lines are 3
Please enter your ID/s:(enter comma separated IDs if more than one):6,7,8,9,10
6 This ID does not exist !
7 The string we do care about.
8 Value
8 Value
8 Value2
9 Value2
10 This ID does not exist !


"""

