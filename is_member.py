#!/usr/bin/env python

"""
Write a function is_member that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)


"""

def is_member(x,a):
   j= len(a)-1
   while (j>0):
     if a[j] == x:
       return True
     j=j-1
     if a[j] != x:
       return False
 
def main():
    v = is_member(3,[1,2,3])
    print v

if __name__ == "__main__":
    main()
