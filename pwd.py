#!/usr/bin/env python

"""
Write a function that prints the present working directoryi

"""

import os

def pwd():
    return os.getcwd()

def main():
    w = pwd()
    print w

if __name__ == "__main__":
    main()

