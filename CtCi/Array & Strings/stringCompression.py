# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# String Compression

import sys

def stringCompression(string):
    i=0
    sol=""
    while i < len(string):
        char = string[i]
        cnt=1
        i+=1
        while i < len(string) and char == string[i]:
            cnt+=1
            i+=1
        sol+=(str(char+str(cnt)))
    # print(sol)
    if len(sol) > len(string):
        return string
    return sol

def stringCompression2(string):
    cnt = 0
    sol = ""
    for i in range(len(string)):
        cnt+=1
        if i+1>=len(string) or string[i] != string[i+1]:
            sol+=(string[i]+str(cnt))
            cnt=0
    if len(sol) > len(string):
        return string
    return sol

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("String not read")
    else:
        string = sys.argv[1]
        print(stringCompression2(string))