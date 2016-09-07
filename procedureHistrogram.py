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
    for i in range(0,len(l)-1):
        for j in l[i]:
            n = l[i]
            v = generate_n_chars(n,c)
        return v

def main():
    k = histogram([4])
    print k

if __name__ == "__main__":
    main()
