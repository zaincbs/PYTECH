#!/usr/bin/env python

"""
Write a python a program that asks user of  filename, creates a
file, ask user its firstname and last name ,writes them in a file
and of course closes it
"""
import sys

def fileUserInput():
    fileName= raw_input("Please enter your file name : ")
    firstName= raw_input("Please enter your first name : ")
    LastName= raw_input("Please enter your last name : ")
    fileObject = open(fileName, 'w')
    fileObject.write(firstName+LastName)
    fileObject.close()

def main():
    fileUserInput()
   
if __name__ == "__main__":
    main()


