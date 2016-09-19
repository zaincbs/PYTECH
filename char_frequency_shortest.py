#!/usr/bin/env python

"""
Write a function char_freq() that takes a string and builds a 
frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary. 
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""
import string

def char_freq(s):
    for letters in string.ascii_lowercase:
        print '{'"'",letters,"':'", s.count(letters),"'",'}',
  
def main():
    calling_function = char_freq("abbabcbdbabdbdbabababcbcbab")

if __name__ == "__main__":
    main()

"""
$ ./char_frequency_another_way.py 
{' a ':' 7 ' } {' b ':' 14 ' } {' c ':' 3 ' } {' d ':' 3 ' }
{' e ':' 0 ' } {' f ':' 0 ' } {' g ':' 0 ' } {' h ':' 0 ' }
{' i ':' 0 ' } {' j ':' 0 ' } {' k ':' 0 ' } {' l ':' 0 ' } 
{' m ':' 0 ' } {' n ':' 0 ' } {' o ':' 0 ' } {' p ':' 0 ' } 
{' q ':' 0 ' } {' r ':' 0 ' } {' s ':' 0 ' } {' t ':' 0 ' }
{' u ':' 0 ' } {' v ':' 0 ' } {' w ':' 0 ' } {' x ':' 0 ' }
{' y ':' 0 ' } {' z ':' 0 ' }
"""
