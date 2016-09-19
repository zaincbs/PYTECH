#!/usr/bin/env python

"""
writing a function that functions as mv command in Linux
e.g. $ mv filename1.txt filename2.txt

So in this function filename1.txt becomes filename2.txt and filename1.txt
gets deleted
"""
import sys
import os
def mv(filename1,filename2):
    fileObj1 = open(filename1, 'r')
    reading = fileObj1.read()
    fileObj2 =open(filename2, 'w')
    fileObj2.write(reading)
    fileObj2.close()
    fileObj1.close()    
    os.remove(filename1)

def main():
    argList = sys.argv
    filename1 = argList[1]
    filename2 = argList[2]
    v = mv(filename1, filename2)  
if __name__ == "__main__":
    main()

