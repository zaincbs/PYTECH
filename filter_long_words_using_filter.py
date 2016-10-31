#!/usr/bin/env python

"""
Using the higher order function filter(), define a function 
filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer
than n.

"""
def filter_long_words(l,n):
    return filter(lambda word: len(word) > n, l)
def main():
    list_with_len_of_word =filter_long_words(['happy','God','Abdul', 'Samad', 'needs', 'a', 'job'],3)
    print list_with_len_of_word

if __name__ == "__main__":
    main()
"""
H$ ./filter_long_words_using_filter.py 
['happy', 'Abdul', 'Samad', 'needs']


"""

