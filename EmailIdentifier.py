#!/usr/bin/python     

"""
Creating an email identifier. It should check that email 
email has a valid descrption
"""
import re
import sys
def emailidenfier(email_id):
    if '@' and '.' in email_id:
            email = re.split(r'[@.]',email_id)
            print email
    if len(email) == 3  and email[2] == 'com':
        return "email id is valid"
    else:
        return "email id is not valid"
def main():
    my_List= sys.argv
    email_address= my_List[1]
    em= emailidenfier(email_address)
    print em

if __name__ == "__main__":
    main()
"""
$ ./EmailIdentifier.py  'asmad@ymail.com'
['asmad', 'ymail', 'com']
email id is valid

$ ./EmailIdentifier.py  'asmad@ymail.com.sdvnsd '
['asmad', 'ymail', 'com', 'sdvnsd ']
email id is not valid

 $ ./EmailIdentifier.py 'asamad@tvu.comvdtgd'
 ['asamad', 'tvu', 'comvdtgd']
 email id is not valid

"""
