#!/usr/bin/env python
# -*- decoding: latin-1 -*-

"""
Represent a small bilingual lexicon as a Python dictionary in
the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"år"} and use it to translate your 
Christmas cards from English into Swedish.

Use the higher order function map() to write a function
translate() that takes a list of English words and returns a
list of Swedish words.
"""
my_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
def translate(l):
    def diclist(): return (l for l in  my_dict.values())
    #f =dict[(map(,my_dict))]
    #print f


    #for k,v in dic.items():
    #    print k

def main():
    v = translate(["merry", "christmas", "and", "happy", "new", "year"])
    


if __name__ == "__main__":
    main()

    
