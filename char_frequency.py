#!/usr/bin/env python

"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").



"""
from collections import Counter

def char_freq(s):
    newsorted_string= ''.join(sorted(s))
    elements = 'abcdefghijklmnopqrstuvwxyz'
    splitting_elements = elements.split()
    
    #return Counter(newsorted_string)

    
def main():
    v = char_freq("abbabcbdbabdbdbabababcbcbab")
    print v

if __name__ == "__main__":
    main()


