#!/usr/bin/env python

"""
Create afile that takes two input: 1.filename, 2.string
file name is samad.txt, string is "my name is Abdul Samad"
then it should create the file
"""
import sys

def cat_2(filename,string_to_be_written_in_file):
    fileObject= open(filename ,"w")
    fileObject.write(string_to_be_written_in_file)
    fileObject.close()

def main():
    argList = sys.argv
    filename=argList[1]
    string_to_be_written_in_file = argList[2]
    cat_2(filename,string_to_be_written_in_file)
if __name__ == "__main__":
    main()
    
