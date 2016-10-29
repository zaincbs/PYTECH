#!/usr/bin/env python

"""
Write a program that maps a list of words into a list of 
integers representing the lengths of the correponding words.
Write it in three different ways:
1) using a for-loop, 
2) using the higher order function map(), and
3) using list comprehensions.


"""
def Using_for_loop(l):
    for i in l:
        print 'The length of', "'", i,"'",'is :', len(i)

def Using_map_function(l):
    def length(x):  return "The length of",x,'is',len(x)
    return map(length,l)

def Using_List_Comprehension(l):
    
    length_of_list_tokens= ([len(token) for token in l])
    return length_of_list_tokens
    
def main():
    print 'Using For Loop:'
    v = Using_for_loop(['happy','God','Abdul', 'Samad', 'needs', 'a', 'job'])
    print'\n' 

    print 'Using Map Function:'
    k = Using_map_function(['happy','God','Abdul', 'Samad', 'needs', 'a', 'job'])
    print k
    print'\n' 

    print "Using List Comprehension"
    q = Using_List_Comprehension(['happy','God','Abdul', 'Samad', 'needs', 'a', 'job'])
    print q


"""    
$ ./Mapping_List_Of_Words.py 
Using For Loop:
The length of ' happy ' is : 5
The length of ' God ' is : 3
The length of ' Abdul ' is : 5
The length of ' Samad ' is : 5
The length of ' needs ' is : 5
The length of ' a ' is : 1
The length of ' job ' is : 3


Using Map Function:
[('The length of', 'happy', 'is', 5), ('The length of', 'God', 'is', 3), ('The length of', 'Abdul', 'is', 5), ('The length of', 'Samad', 'is', 5), ('The length of', 'needs', 'is', 5), ('The length of', 'a', 'is', 1), ('The length of', 'job', 'is', 3)]


Using List Comprehension
[5, 3, 5, 5, 5, 1, 3]

"""
    

if __name__ == "__main__":
    main()

    
