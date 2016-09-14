#!/usr/bin/env python


"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

"""

def map(s):
    list = []
    for i in s:
            list.append(len(i))
    print list

def main():
    map(('good','mad', 'great'))

if __name__ == "__main__":
    main()
"""

[4, 3, 5]

"""
