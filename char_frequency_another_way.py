#!/usr/bin/env python

"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").



"""
import string

def char_freq(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    newsorted_string= ''.join(sorted(s))
    #print newsorted_string
    
    #creating an ascii list of lowercase
    #alphabets
    lowercase_elements_in_ascii =list(string.ascii_lowercase)
    for letters in lowercase_elements_in_ascii:
        print '{'"'",letters,"':'", newsorted_string.count(letters),"'",'}',
  
def main():
    calling_function = char_freq("abbabcbdbabdbdbabababcbcbab")

if __name__ == "__main__":
    main()


