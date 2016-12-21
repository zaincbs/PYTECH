#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Python File Reader
Read in a file of the form:
ID date-time string1 string2 string3
ID is a positive integer, date-time is a string without spaces, and the other three
strings may or may not have spaces. But if they do have spaces, they will have
double quotes around them. Double quotes in a string can be escaped with a
backslash. The fields are space separated (possibly with multiple spaces), and the
records are terminated with a newline character. There may be duplicated records,
in which case both should be stored. All five values must be present for a row to be
valid.
For example:
7 2016-06-10-17:53:22 “A quoted string we don’t care about” “The string we do
care about.” “Another string we don’t care about with escaped\” \” quotes. ”
8 2016-06-10-17:53:22 Str1 Value Str3
8 2016-06-10-17:53:22 Str1 Value Str3
8 2016-06-10-17:53:22 Str1 Value2 Str3
9 2016-06-10-17:53:22 Str1 Value2 Str3
-1 2016-06-10-17:53:22 “This line is invalid” Str2 Str3
10 2016-06-10 17:53:22 “Also invalid” Str2 Str3
10 2016-06-10-17:53:22 “Also invalid” Str2
We want to store the ID value and the string2 value in a local memory data
structure, ideally with fast lookup and insert. Invalid rows should not be stored, but
a count of the total number of invalid lines should be printed out after reading the
whole file.
Now, prompt the user on the command line (using input, raw_input or the
equivalent) for a comma separated list of ids. For each id in that list, print out all of
the id and string2 values from records that have that id. So, with the above example,
an input of: 9,8 should yield:
9 Value2
8 Value
8 Value
8 Value2
If an id has multiple records, they should be printed out in the order that they were
encountered in the original file.
Don’t use anything that is not in the standard libraries.
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
	try:
	    val = int(i)
	except:
	    print i, " 'This ID is not a number. Please enter a valid number. Invalid Entry!'  "
	    continue
        if int(i) not in mydict :
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

$ ./PythonFileReader-new.py examplefile.txt
The number of invalid lines are 3
Please enter your ID/s:(enter comma separated IDs if more than one):7,8,9,sfsf,0,1
7 The string we do care about.
8 Value
8 Value
8 Value2
9 Value2
sfsf  'This ID is not a number. Please enter a valid number. Invalid Entry!'
0 This ID does not exist !
1 This ID does not exist !  
"""

