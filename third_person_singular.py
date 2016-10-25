#!/usr/bin/python

"""
The third person singular verb form in English is
distinguished by the suffix -s, which is added to the stem of
the infinitive form: run -> runs. 
A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s

Your task in this exercise is to define a 
function make_3sg_form() which given a verb in infinitive
form returns its third person singular form.

Test your function with words like try, brush, run and fix. 
Note: however that the rules must be regarded as heuristic,
in the sense that you must not expect them to work for all
cases. 

Tip: Check out the string method endswith().
"""

import re
import sys
def make_3sg_form(s):
    chars_in_ends = ['o','ch','s','sh','x','z']
    for c in chars_in_ends:
        if s.endswith(c):
            d = s + 'es'
            return d
    if s.endswith('y'):
        return s.replace('y','ies')
    #if s[-1] ==  'o' OR 'ch' OR 's' OR 'sh' OR 'x' OR 'z':
    #`    return s.replace(s[-1],'es')
    else:
        ch = s + 's'
        return ch

def main():
    my_List= sys.argv
    word= my_List[1]
    b = make_3sg_form(word)
    print b

if __name__ == "__main__":
    main()

"""
$ ./third_person_singular.py brush
brushes

$ ./third_person_singular.py run
runs

$ ./third_person_singular.py try
tries

$ ./third_person_singular.py fix
fixes

$ ./third_person_singular.py word
words

"""
    
