#!/usr/bin/env python
"""

Write a function that returns all the files present in a 
current directory

"""
import os

def lsFunction():
    for x in os.listdir('./'):
        print x
       

def main():
    v = lsFunction()
    print v

if __name__ == "__main__":
    main()
