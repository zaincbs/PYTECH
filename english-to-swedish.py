#!/usr/bin/env python      
# -*- decoding: latin-1 -*-
"""
Represent a small bilingual lexicon as a Python dictionary in the

following fashion:


and use it to translate your Christmas cards 

from English into Swedish. 

That is, write a function translate() that takes a list of

English words and returns a list of Swedish words.


"""

def translate(eng_list):
    swe = [] 
    swedish_meanings = ("god", "jul", "och", "gott", "nytt","år")
    for words in swedish_meanings:
        swe.append(words)
    return swe

def main():
    v= translate("merry","christmas","and","happy","new","year")
    print v

if __name__ == "__main__":
        main()
