#!/usr/bin/env python

"""Creating a python function that functions as 
cp command in linux command line e.g cp filename1 filename2.
filename 2 should depict all the contents of filename 1"""

import sys

def cpFunction(filename,filename1):
    fileObj =open(filename,'r')
    v=fileObj.read()
    fileObj1=open(filename1,'w')
    fileObj1.write(v)
    fileObj.close()
    fileObj1.close()
def main():
    argList= sys.argv
    filename = argList[1]
    filename1 = argList[2]
    cpFunction(filename, filename1)

if __name__ == "__main__":
    main()

"""
$ ./cpFuntion.py Samadcp.txt Samad.txt 

$cat Samad.txt 
I am Abdul Samad

$ cat Samadcp.txt 
I am Abdul Samad
"""
