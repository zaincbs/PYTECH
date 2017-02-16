#!/usr/bin/env python

"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

"""

def get_middle(s):
    #your code here
    length = len(s)
    mid =len(s)/2
    if length%2 == 1:
    	return s[mid]
    else:
    	return s[mid-1]+s[mid]

def main():
    print get_middle("test")
    print get_middle("testing")
    print get_middle("middle")
    print get_middle("bungee")
    print get_middle("A")
    print get_middle("of")
    


if __name__ == "__main__":
    main()
