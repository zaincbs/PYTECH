#!/usr/bin/env python

"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
"aa11" -> 2 # 'a' and '1'

Example Tests:
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)

"""
import string
def duplicate_count(text):
    # Your code goes here
    count = 0	
    s= '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for x in s:
        if text.count(x)>1:
           # print x, x.count(x)
	   count = count + 1

    if count <= 1:	
        print "The repeated alphabets/numbers in","'",text,"'","is: " , count
    else:
        print "The frequency of repeated  alphabets/numbers in","'",text,"'","are:" , count


def main():
     v = duplicate_count('abcdea')
     m = duplicate_count('indivisibility')
     k=  duplicate_count('abcde')
     l = duplicate_count('indivisibilities')
     m = duplicate_count('aa11')


if __name__ == "__main__":
    main()

"""
$ ./CountingDuplicates.py
The repeated alphabets/numbers in ' abcdea ' is:  1
The repeated alphabets/numbers in ' indivisibility ' is:  1
The repeated alphabets/numbers in ' abcde ' is:  0
The frequency of repeated  alphabets/numbers in ' indivisibilities ' are: 2
The frequency of repeated  alphabets/numbers in ' aa11 ' are: 2   


"""
