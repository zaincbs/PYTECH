#!/usr/bin/env python

"""

Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

"""
number = 0

def max_of_three(n1,n2,n3):
	if (n2>n1) and (n2 >n3):
		number = n2
	elif(n3>n2) and (n3>n1):
		number = n3
	elif(n1 > n2) and (n1>n3): 
		number = n1
	return number

def main():
	n = max_of_three(10,12,30)
	print n , "is the largest number"

if __name__ == "__main__":
    main()

