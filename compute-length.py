#!/usr/bin/env python      


"""
Define a function that computes the length of a given list or string.

"""
x=0 
def lengthOfStrOrList(input):
    count =0
    for x in input:
        count = count + 1
    return count
"""
Define counting variable inside a function
since it is counting inside a iterative loop,
which is further inside a function.
"""


def main():
	s = lengthOfStrOrList(("input"))
	print "The length is", s
if __name__ == "__main__":
    main()

