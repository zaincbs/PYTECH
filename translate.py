#!/usr/bin/env python

"""Write a function translate that

double every consonant and place an occurrence of "o" in between.

For example, translate("this is fun") should return the string "tothohisos isos fofunon".
"""
def translate(s):
    vowel = ["a","e","i","o","u"," "]
    s_n = ""
    for x in s:
        if x not in vowel:
            s_n = s_n +  x + 'o' + x
        elif x in vowel:
            s_n = s_n + x
    return s_n

def main():
    v = translate("this is fun")
    print v


if __name__ == "__main__":
    main()

