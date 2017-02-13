#!/usr/bin/env python

"""
You are given an array (which will have a length of at least 3,
but could be very large) containing integers. The array is eith
er entirely comprised of odd integers or entirely comprised of 
even integers except for a single integer N. Write a method th
at takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160

"""

def find_outlier(integers):
    sum = 0   #sum of elements in integers
    for s in integers:
        sum = sum + s
        #print sum
    for i in integers:
        if i%2!=0 & (sum-i)%2==0:
            return i,"is an odd element"
        if i%2==0 & (sum-i)%2!=0: 
            if len(integers)%2 == 0:
                return i,"is an even element"
        if i%2==0 & (sum-i)%2==0: 
            if len(integers)%2 != 0:
                return i,"is an even element"

                
def main():
    v = find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])   
    print v  #return 11
    j = find_outlier([160, 3, 1719, 19, 11, 13, -21])   
    print j  #return 160
if __name__ == "__main__":
    main()

"""
$ ./UniqueEvenOrOddFromAList.py 
(11, 'is an odd element')
(160, 'is an even element')



"""
