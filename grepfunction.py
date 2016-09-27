#!/usr/bin/env python
"""
Write a grep function that searches for a string
in a file


"""
import sys
def grepfunction(filename, searchstr):
    f= open(filename,'r')
    for lines in f:
        #print lines
	if searchstr in lines:
           #print lines
	   #print"\033[44;33m%s\033[m"% (searchstr), lines
	   print lines.replace(searchstr,"\033[44;33m%s\033[m"% (searchstr))	

	#\033[44;33m%s\033[m  highlights theword in the line
	#ref: http://stackoverflow.com/questions/35731194/how-to-highlight-a-word-found-in-a-text-file
def main():
    argList= sys.argv
    filename_to_be_read = argList[1]
    string_to_be_searched= argList[2]
    v = grepfunction(filename_to_be_read, string_to_be_searched)
   # print v

if __name__ == "__main__":
    main()
""" 
$ cat Samadnew.txt
I am Abdul Samad.
I happen to live in California

I happen to live in California

I work at TVU Networks                 
-------
$ ./grepfunction.py Samadnew.txt "in California"
I happen to live in California   

$ ./grepfunction.py Samadnew.txt Samad
I am Abdul Samad.                   
                                    
$ ./grepfunction.py Samadnew.txt Networks
I work at TVU Networks              

$ ./grepfunction.py Samadnew.txt "in California"
I happen to live in California

I happen to live in California                                      
"""
