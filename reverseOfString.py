#!/usr/bin/env python

"""
Define a function reverse, that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

"""

def reverse(s):
    k= ""
    for i in range (len(s)-1, -1, -1):
      k = k + s[i]
    return k

def main():
    v = reverse("This is testing")
    print v

if __name__ == "__main__":
    main()

