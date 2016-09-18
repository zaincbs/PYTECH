#!/usr/bin/env python

"""
A pangram is a sentence that contains all the letters
of the English alphabet at least once 

for example: The quick brown fox jumps over the lazy dog.

Your task here is to write a function to check a sentence 

to see if it is a pangram or not

"""


def pangram(s):
    a = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'

    #removing characters from a string
    for i in s:    
        if i == ',': 
            a = s.replace(i, "")
        if i == " ":
            a = s.replace(i, "")
        if i == "'":
            a = s.replace(i, "")
        if i == "?":
            a = s.replace(i, "")
        if i == ".":
            a = s.replace(i, "")
        if i == '!': 
            a = s.replace(i, "")
            
    #sorting string alphabetic order and in lowercase
    newstring = ''.join(sorted(a)).lower() 
    sorting_newstring = ''.join(sorted(newstring))
    #print sorting_newstring

    #removing duplicates from sorting_newstring   
    removing_duplicates = set(sorting_newstring)
    rearranging_removed_duplicates= ''.join(sorted(removing_duplicates))
    #print rearranging_removed_duplicates

    if rearranging_removed_duplicates == letters:
        return s, " is a pangram"
    else:
        return s, " is not a pangram"

def main():
    v = pangram("The quick brown fox jumps over the lazy dog.")
    print v
    v = pangram("Pack my box with five dozen liquor jugs.")
    print v
    v = pangram("Jackdaws love my big sphinx of quartz.")
    print v
    v = pangram("The five boxing wizards jump quickly.")
    print v
    v = pangram("How vexingly quick daft zebras jump!")
    print v

if __name__ == "__main__":
    main()

        
"""
$ ./pangrams.py 
('Thequickbrownfoxjumpsoverthelazydog', ' is a pangram')
('Packmyboxwithfivedozenliquorjugs', ' is a pangram')
('Jackdawslovemybigsphinxofquartz', ' is a pangram')
('Thefiveboxingwizardsjumpquickly', ' is a pangram')
('Howvexinglyquickdaftzebrasjump', ' is a pangram')
"""
