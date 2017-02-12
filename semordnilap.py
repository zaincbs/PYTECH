#!/usr/bin/env python
"""
According to Wikipedia, a semordnilap is a word or phrase that spel
ls a different word or phrase backwards. ("Semordnilap" is itself "
palindromes" spelled backwards.) Write a semordnilap recogniser tha
t accepts a file name (pointing to a list of words) from the user 
and finds and prints all pairs of words that are semordnilaps to th
e screen. For example, if "stressed" and "desserts" is part of the
word list, the the output should include the pair "stressed dessert
s". Note, by the way, that each pair by itself forms a palindrome!

"""
import sys
def semordnilap_recogniser(filename):

    f = open(filename,'r').readlines()
    #reading lines

    lines = [s.rstrip() for s in f]
    #stripping the \n from the elements in readlines()

    print lines


def main():
    myList= sys.argv
    txtfile=myList[1]
    v = semordnilap_recogniser(txtfile)


if __name__ == "__main__":
    main()

