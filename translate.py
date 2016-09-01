#!/usr/bin/env python



def translate(s):
    vowel = ["a","e","i","o","u"]
    index = 0
    for x in range(len(s) ):
        letter = s[index]
        if s in vowel:
            continue
        elif s not in vowel:
           a=s[x]+ s.join("o")+s[x]
        index = index + 1                
    return a
        


def main():
    v = translate("This is fun")
    print v

if __name__ == "__main__":
    main()
