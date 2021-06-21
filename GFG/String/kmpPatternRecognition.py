# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
'''

# Time Complexity: O(n) n is txt size

class Solution:
    def computeLSA(self, pat):
        lps = [0] * len(pat)
        j = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[j] = 0
                    i += 1
        return lps
    
    def search(self, pat, txt):
        lps = self.computeLSA(pat)
        i = 0
        j = 0
        N = len(txt)
        M = len(pat)
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == M:
                print("Found at ", i-j)
                j = lps[j-1]
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                    
if __name__ == '__main__':
    Solution().search('AABA', 'AABAACAADAABAABA')