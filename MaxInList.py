#!/usr/bin/env python

"""



The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

"""
def max_in_list(l):
	l.sort()
	return l[len(l)-1]
def main():
	v = max_in_list([10,40,20,04,30,50])
	print v,"is the largest number"

if __name__ == "__main__":
	main()
