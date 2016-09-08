#!/usr/bin/env python

"""Write a python function that returns
a cat function i.e. it displays a file's contents
"""
import sys

def cat(fileName,mod):
	fileObj = open(fileName,mod)
	v =fileObj.read()	
	print v
	fileObj.close()


def main():
	argList =sys.argv
	cat(argList[1],argList[2])

if __name__ == "__main__":
	main()





