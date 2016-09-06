#!/usr/bin/env python
"""
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
"""

def overlapping(l1,l2):
    i =  len(l1)-1
    j =  len(l2)-1
    while (i>=0):
        while (j>=0):
            if l1[i]==l2[j]:
                return True
            if l1[i]!=l2[j]:
                j = j - 1
        i = i-1
    return False


def main():
    v=overlapping([1],[2,1,3])
    print v

if __name__ == "__main__":
    main()
