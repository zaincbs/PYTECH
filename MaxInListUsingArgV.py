#!/usr/bin/env python

"""



The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

"""
import sys

def max_in_list(l):
	v = sorted(l)	
	return v
	#return l[len(l)-1]
def main():
	i = 2  
        while (i <= 5):
		print max_in_list(sys.argv[i])
		i = i -1 
if __name__ == "__main__":
	main()
