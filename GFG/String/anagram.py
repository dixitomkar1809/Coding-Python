# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
'''
from collections import Counter
class Solution:
    def getAnagram(self, s1, s2):
        return Counter(s1) == Counter(s2)

if __name__=='__main__':
    s1 = 'geeksforgeeks'
    s2 = 'forgeeksgeeks'
    s3 = 'allergy'
    s4 = 'allergic'
    sol = Solution()
    print(sol.getAnagram(s3, s4))