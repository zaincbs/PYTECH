#!/usr/bin/env python      

"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.


"""
def vowelFunction(s):
    vowel = ['a','e','i','o','u']
    if s not in vowel:
        return False
    else:
        return True

def main():
    t = vowelFunction('b')
    print t

if __name__ == "__main__":
    main()
