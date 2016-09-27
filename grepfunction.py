#!/usr/bin/env python
"""
Write a grep function that searches for a string
in a file


"""

def grepfunction(filename, searchstr):
    f= open(filename,'r')
    for lines in f:
        #print lines
	if searchstr in lines:
          print lines
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

I work at TVU Networks                 
-------
$ ./grepfunction.py Samadnew.txt "in California"
I happen to live in California   

$ ./grepfunction.py Samadnew.txt Samad
I am Abdul Samad.                   
                                    
$ ./grepfunction.py Samadnew.txt Networks
I work at TVU Networks              

$ ./grepfunction.py Samadnew.txt California
I happen to live in California    
"""
