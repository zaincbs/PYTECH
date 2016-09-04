#!/usr/bin/env python

"""
Define a function is_palindrome that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.


"""

from reverseOfString import reverse

def palindrome(s):
    if s == reverse(s):
        return True
    else:
        return False

def main():
    p = palindrome("ana")
    print p

if __name__ == "__main__":
    main()

