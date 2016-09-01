#!/usr/bin/env python


"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.


"""

def sum(s):
    add = 0
    for x in s:
     add = add + x
    return add

def multiply(s):
    mul = 1
    for x in s:
     mul= mul *x 
    return mul

def main():
    ad = sum([1, 2, 3, 4])
    print "sum function returns", ad
    mu = multiply([1, 2, 3, 4 ])
    print "multiply function returns", mu

if __name__ == "__main__":
    main()


