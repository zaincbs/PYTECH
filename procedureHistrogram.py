#!/usr/bin/env python

"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
"""

from generateCharacters import *

def histogram(l):
    c ='x'
    b = len(l)-1
    for j in l:
        v = generate_n_chars(j,c)
    return v

def main():
    k = histogram([4,9,7])
    print k

if __name__ == "__main__":
    main()
