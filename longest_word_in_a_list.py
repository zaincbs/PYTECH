#!/usr/bin/env python

"""

Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

"""

def find_longest_word(s):
    list=[] 
    for i in s:
        list.append(len(i))
    list.sort()
    return list[len(list)-1] 

def main():
    longest_word-s-length= find_longest_word(['good','mad', 'great'])
    print longest_word-s-length    

if __name__ == "__main__":
    main()

"""
$ ./longest_word_in_a_list.py 
5
"""

