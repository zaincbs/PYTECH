import sys

def readopp(filename):
    l= ''
    strn=''
    newstr = ''
    with open(filename, 'r') as f:
        lines=f.readline()
        print lines.reverse()
        print ('')
        for i in range(0,len(lines)-1):
            strn = strn +lines[i] 
        print strn
        for j in range(len(strn)-1,-1,-1):
            newstr= newstr + strn[j]
        print newstr

        #for line in f:
        #   j = j + line
        #   j.strip()
        #print j

def main():
    argList= sys.argv
    filename = argList[1]
    readopp(filename)

if __name__ == "__main__":
    main()

