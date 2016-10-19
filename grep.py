#!/usr/bin/env python

"""
Write a python function that works as grep function of Linux
e.g. $ grep mv mv.py 
writing a function that functions as mv command in Linux
e.g. $ mv filename1.txt filename2.txt
def mv(filename1,filename2):
    v = mv(filename1, filename2)  


The program should return the lines/text which had 'mv' string in
them.
"""
import sys

def grep(file1):
    fileObj= open(file1, 'r')
    reading_file = file1.read(fileObj)
    print reading_file
    with fileObj as f:
        for line in f:        
            print line
def main():
    argList = sys.argv
    #line = argList[1]
    file_to_be_read = argList[1]

           
if __name__ == "__main__":
    main()


