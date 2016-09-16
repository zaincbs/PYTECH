#!/usr/bin/env python

"""
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""

def filter_long_words(list_of_words, n):
    list = []    
    for i in list_of_words:
        if len(i) > n:
            list.append(i)
    return list

def main():
   sending_values_to_function=  filter_long_words(('good','mad', 'great'), 3)
   print sending_values_to_function

if __name__ == "__main__":
    main()

"""
$ ./filter_long_words.py 
['good', 'great']
"""
