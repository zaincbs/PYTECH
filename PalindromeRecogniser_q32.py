#!/usr/bin/env python

"""
Write a version of a palindrome recogniser that i
accepts a file name from the user, reads each line,
and prints the line to the screen if it is a palindrome.
"""
from reverseOfString import reverse
from palindrome_recog import palindrome_recognizer
import sys 


def acceptFile(filename):
    f= open(filename,'r').readlines()
    #readlines() produces a list of lines separated by cooma's and endswith \n
    #we need rstrip() to remove \n from 'f'

    stripped_line= [s.rstrip() for s in f]
    #we need a for loop that iterates over every element in the list and see if the 
    #line/element of a list is palindrome or not

    for i in stripped_line:
        if i in palindrome_recognizer(i):
	    print i," : this line is a palindrome"
	else:
	    print i," : this line is not a palindrome"

def main():
    myList=sys.argv
    txtfile = myList[1]
    v = acceptFile(txtfile)
if __name__ == "__main__":
    main()

