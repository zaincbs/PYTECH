#!/usr/bin/env python

"""

Reversing the text in a file
"""
import sys 


def reverseFile(filename):
    f = open(filename,'r')
    for line in f:
        line = line[::-1]
	print line
    f.close()


def main():
    argList= sys.argv
    file_to_be_read = argList[1]
    v = reverseFile(file_to_be_read)
                                                            
if __name__ == "__main__":
    main()

"""
$ ./ReverseFile.py feed.text

god yzal eht revo spmuj xof nworb kciuq ehT 

"""
