#!/usr/bin/env python

"""
Write a version of a palindrome recogniser that i
accepts a file name from the user, reads each line,
and prints the line to the screen if it is a palindrome.
"""
#from reverseOfString import reverse
#from palindrome_recog import palindrome_recognizer
import sys 


def acceptFile(filename):
    f= open(filename,'r').readlines()
    #readlines() produces a list of lines separated by cooma's and endswith \n
    #we need rstrip() to remove \n from 'f'

    lines= [s.rstrip() for s in f]
    #we need a for loop that iterates over every element in the list and see if the 
    #line/element of a list is palindrome or not

    letter = "qwertyuiopasdfghjklzxcvbnm"
    for line in lines:
        st = ""
        for ch in line.lower():
            if ch in letter:
                st += ch
        is_palindrome = True
        for i in range(len(st)/2):
            if st[i] != st[len(st) - i - 1]:
                is_palindrome = False
                print line," : this line is not a palindrome"
                break
        if is_palindrome:
                print line," : this line is a palindrome"
            
             
    """

    for ln in lines:
        if ln[1::] == ln[len(ln)-1:-len(ln)-1:-1]:
	        print ln," : this line is a palindrome"
        else:    
	        print ln," : this line is not a palindrome"
    f.close()            
     """       
def main():
    myList=sys.argv
    txtfile = myList[1]
    v = acceptFile(txtfile)
if __name__ == "__main__":
    main()
"""
$ ./PalindromeRecogniser_q32.py Samad.txt 
I am Abdul Samad  : this line is not a palindrome
Don't nod.  : this line is a palindrome
I did, did I?  : this line is a palindrome
My gym  : this line is a palindrome
Red rum, sir, is murder  : this line is a palindrome
Step on no pets  : this line is a palindrome
Top spot  : this line is a palindrome
Was it a cat I saw?  : this line is a palindrome
Eva, can I see bees in a cave?  : this line is a palindrome
No lemon, no melon  : this line is a palindrome






"""
