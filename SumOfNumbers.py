#!/usr/bin/env python

"""
Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!
"""

def get_sum(a,b):
    #good luck!
    sum = 0
    if a == b:
    	return "Since both are same"
    elif b>a:
        for i in range(a,b):
    	    sum = sum + i
        return sum + b
    else:
	for i in range(a,b,-1):
	    sum = sum + i 
	return sum + b


def main():
    print get_sum(1, 0)
    print get_sum(1, 2)
    print get_sum(0, 1)
    print get_sum(1, 1) 
    print get_sum(-1, 0) 
    print get_sum(-1,2)
    print get_sum(-1,5)
    print get_sum(5,-1)
    print get_sum(-1,-3)
    print get_sum(-3,-1)
    print get_sum(-3,-3)
    
	


if __name__ == "__main__":
    main()


