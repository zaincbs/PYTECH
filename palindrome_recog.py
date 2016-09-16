#!/usr/bin/env python

"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
"""

from reverseOfString import reverse

def palindrome_recognizer(s):
    punctuation = ' 0123456789!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    for i in s:    
        if i in punctuation:
            a = s.replace(i, "")
    v=a.lower()        
    print v
    v1 =len(v)/2
    if v[v1:len(v)] == reverse(v[0:v1]):
        return s," is a palindrome phrase"
    else:
        return s," is not a palindrome phrase" 

def main():
    b = palindrome_recognizer("Step on no pets")
    print b

if __name__ == "__main__":
    main()

"""
./palindrome_recog.py 
steponnopets
('Step on no pets', ' is a palindrome phrase')
"""
