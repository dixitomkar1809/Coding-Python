# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
'''
    
# Time Complexity: O(M+N) M is lenght of pattern, N is length of main string 
    
def solution(mainString, pattern):
    lps = generateLSA(pattern)
    i = 0
    j = 0
    while i < len(mainString):
        if mainString[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print("Found at: " + str(i-j))
            j = lps[j-1]
        elif i < len(mainString) and mainString[i] != pattern[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
def generateLSA(pattern):
    lps = [0] * len(pattern)
    prefixLength = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prefixLength]:
            prefixLength += 1
            lps[i] = prefixLength
            i += 1
        else:
            if prefixLength != 0:
                prefixLength = lps[prefixLength - 1]
            else:
                i += 1
    return lps

if __name__=="__main__":
    solution('ABABDABACDABABCABAB', 'ABABCABAB')
    solution('AABAACAADAABAABA', 'AABA')