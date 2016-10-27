#!/usr/bin/python

"""
 In English, the present participle is formed by adding the 
 suffix -ing to the infinite form: go -> going. 
 A simple set of heuristic rules can be given as follows:
  If the verb ends in e, drop the e and adding
  (if not exception: be, see, flee, knee, etc.)
  
  If the verb ends in ie, change ie to y and add ing
  
  For words consisting of consonant-vowel-consonant, double the
  final letter before adding ing
  
  By default just add ing
  
  Your task in this exercise is to define a function
  make_ing_form() which given a verb in infinitive form returns
  its present participle form.
  
  Test your function with words such as lie, see, move and hug. 
  However, you must not expect such simple rules to work for all 
  cases.

"""
import re
import sys
def make_ing_form(s):
    ch = ''
    cvc = ['a','e','i','o','u']
    if s[-2:] == 'ie':
       return s.replace(s[-2:],'ying')
    if s[-1]=='e' :
        ch = s.replace(s[-1],'')  + 'ing'
        return ch
    for i in cvc:
        if i in s[1]:
            return s + s[-1] +'ing'
    else:
        return s + 'ing'

def main():
    myList = sys.argv
    verb = myList[1]
    calling_function= make_ing_form(verb)
    print  calling_function

if __name__ == "__main__":
    main()
"""    
$ ./Present_Participle.py lie
lying

$ ./Present_Participle.py see
seeing

$ ./Present_Participle.py hug
hugging

$ ./Present_Participle.py move
moving  #this can be an exception


"""
