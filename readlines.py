#!/usr/bin/env python
"""
I am making a function that prints file in reverse order and then reverses
the order of the words

"""  

import sys

def readFile(filename):
    rorder = ''
    opposed = ''
    finale= ''

    #reading file line by line
    with open(filename) as f:
	lines = f.readlines()
    #print lines 

    #printing file in reverse order
    for rev in range(len(lines)-1,-1,-1):
	rorder = rorder + lines[rev]
    #print rorder

    #printing words in reverse order
    for words_rorder in range(len(rorder)-1,-1,-1):
        finale = finale + rorder[words_rorder]
    print finale
def main():
    argList= sys.argv
    filename_to_be_read = argList[1]
    v = readFile(filename_to_be_read)
   # print v

if __name__ == "__main__":
    main() 

"""

$ cat abc.txt
abc zed
I am funny
stop teasing me, please


Where am I?
Who am I
?

blah blah blah                       

$ ./readlines.py abc.txt

dez cba
ynnuf ma I
esaelp ,em gnisaet pots


?I ma erehW
I ma ohW
?

halb halb halb                              

"""
