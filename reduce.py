#!/usr/bin/env python

"""
Using the higher order function reduce(), write a function
max_in_list() that takes a list of numbers and returns the 
largest one.
Then ask yourself: why define and call a new function,
when I can just as well call the reduce() function directly?

"""

def reduce_the_list(l):
    f = lambda a,b : a if (a>b) else b
    return reduce(f,l)

def main():
    finding_the_max_in_list =  reduce_the_list([9,8,4,0,12,-1])
    print  finding_the_max_in_list

if __name__ == "__main__":
    main()

"""
$ ./reduce.py 
12


"""
