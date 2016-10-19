#!/usr/bin/env python
import sys
def readopp(filename):
    f1 = open(filename,'r')
    list = []
    for line in f1:
        line = line.replace("\n", "")
        if line[0] is not '#':
            line = line[::-1]
        list.append( line )
    f1.close()
    print list

    total_lines = len( list ) 

    for x in range( 0, ( total_lines / 2 ) - 1 ):
       if list[ x ][0] is not '#' and list[ total_lines - 1 ][0] is not  '#':  
          list[ x ], list[ total_lines - 1 ] = list[ total_lines - 1], list[ x ] 
    print list
    for lines in list:
        print lines
        
def main():
    argList= sys.argv
    file_to_be_read = argList[1]
    v = readopp(file_to_be_read)
                                                            
if __name__ == "__main__":
    main()

"""
$ cat roku.txt 
abc 123 xyz
567 ytf ju
#hgt asdfa
y 768 agc

$ ./rokupro.py roku.txt 
cga 867 y
uj fty 765
#hgt asdfa
zyx 321 cba

"""
