#!/usr/bin/env python

"""
Write a function find_longest_word() that takes a list of
words and returns the length of the longest one.

Use only higher order functions.

"""
def list_with_len_of_words(l):
    li = []
    for i in l:
        li.append(len(i))
    return li
    
def reducing_into_the_max(l):
    f= lambda a,b: a if (a > b) else b
    return reduce(f,list_with_len_of_words(l))

def main():
    list_with_len_of_word =  reducing_into_the_max(['happy','God','Abdul', 'Samad', 'needs', 'a', 'job'])
    print "The longest word in a list has a length of ",list_with_len_of_word

if __name__ == "__main__":
    main()

"""
$ ./find_longest_word.py 
The longest word in a list has a length of  5

"""
