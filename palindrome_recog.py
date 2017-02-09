#!/usr/bin/env python

"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
"""

from reverseOfString import reverse

def palindrome_recognizer(s):
    for i in s:    
        if i == ',': 
            s = s.replace(i, "")
        if i == " ":
            s = s.replace(i, "")
        if i == "'":
            s = s.replace(i, "")
        if i == "?":
            s = s.replace(i, "")
        if i == ".":
            s = s.replace(i, "")
        if i == '!': 
            s = s.replace(i, "")
    v=s.lower()    
    #print v
    if v == reverse(v):
        return s," is a palindrome phrase"
    else:
        return s," is not a palindrome phrase" 

def main():
    b =palindrome_recognizer("Step on no pets")
    print b
    c =palindrome_recognizer("Go hang a salami I'm a lasagna hog.")
    print c
    d =palindrome_recognizer("Was it a rat I saw?")
    print d
    e =palindrome_recognizer("Step on no pets")
    print e
    f =palindrome_recognizer("Sit on a potato pan, Otis")
    print f
    g =palindrome_recognizer("Lisa Bonet ate no basil")
    print g
    h =palindrome_recognizer("Satan, oscillate my metallic sonatas")
    print h
    i=palindrome_recognizer("I roamed under it as a tired nude Maori")
    print i
    j=palindrome_recognizer("Rise to vote sir")
    print j
    k= palindrome_recognizer("Dammit, I'm mad!")
    print k

if __name__ == "__main__":
    main()

"""
$ ./palindrome_recog.py 
steponnopets
('Steponnopets', ' is a palindrome phrase')
gohangasalamiimalasagnahog
('GohangasalamiImalasagnahog', ' is a palindrome phrase')
wasitaratisaw
('WasitaratIsaw', ' is a palindrome phrase')
steponnopets
('Steponnopets', ' is a palindrome phrase')
sitonapotatopanotis
('SitonapotatopanOtis', ' is a palindrome phrase')
lisabonetatenobasil
('LisaBonetatenobasil', ' is a palindrome phrase')
satanoscillatemymetallicsonatas
('Satanoscillatemymetallicsonatas', ' is a palindrome phrase')
iroamedunderitasatirednudemaori
('IroamedunderitasatirednudeMaori', ' is a palindrome phrase')
risetovotesir
('Risetovotesir', ' is a palindrome phrase')
dammitimmad
('DammitImmad', ' is a palindrome phrase')


"""
