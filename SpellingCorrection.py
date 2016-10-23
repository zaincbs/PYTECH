#!/usr/bin/python  

"""
Define a simple "spelling correction" function correct() that takes
a string and sees to it that:
1) two or more occurrences of the
space character is compressed into one, and
2) inserts an extra space after a period if the period is directly
followed by a letter.
E.g. correct("This   is  very funny  and    cool.Indeed!")
should return "This is very funny and cool. Indeed!" 
Tip: Use regular expressions!
"""
import sys
def correct(s):
    string_withOut_extra_spaces=''
    t= s.split()
    for spaces in t:
        string_withOut_extra_spaces= string_withOut_extra_spaces +" " + spaces   
   # print string_withOut_extra_spaces
    if '.' in string_withOut_extra_spaces:
        index = string_withOut_extra_spaces.find('.')            
        output = string_withOut_extra_spaces[:index+1] + " " +string_withOut_extra_spaces[index+1:]
    return output

def main():
    myString = sys.argv
    line =myString[1]
    The_Line = correct(line)
    print The_Line

if __name__ == "__main__":
    main()
        
"""

$ ./SpellingCorrection.py "This   is  very funny  and    cool.Indeed!"
 This is very funny and cool. Indeed!

"""
   

