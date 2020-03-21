# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''

from collections import Counter
import sys

"""
Time Complexity: O(n)
"""
def checkPermutation(s1, s2):
    return Counter(s1)==Counter(s2)

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Strings Not Detected")
    else:
        print(checkPermutation(str(sys.argv[1]), str(sys.argv[2])))

