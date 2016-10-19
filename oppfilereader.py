import sys

def readopp(filename):
    j= ''
    
    fileobj = open(filename,'r')
    filereader = fileobj.read()
    #print filereader 
                    
    for i in range(len(filereader)-1,-1,-1):
        j = j+ filereader[i]
    print j
    fileobj.close()
                                            
def main():
    argList= sys.argv
    file_to_be_read = argList[1]
    readopp(file_to_be_read)
                                                            
if __name__ == "__main__":
    main()
