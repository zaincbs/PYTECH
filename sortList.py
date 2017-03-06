#!/usr/bin/env python

def sortingAnArray(l):
    reversearray=sorted(l)
    return reversearray
   
  
def main():
    v = sortingAnArray([20, 15,6,71,10,51])
    print v


if __name__ == "__main__":
    main()

"""
$ ./sortList.py 
[6, 10, 15, 20, 51, 71]


"""
