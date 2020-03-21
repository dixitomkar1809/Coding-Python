# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''

from collections import Counter
import sys

def oneWay(str1, str2):
    index1=0
    index2=0
    s1 = str1 if len(str1) < len(str2) else str2
    s2 = str2 if len(str1) < len(str2) else str1
    foundDiff = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if foundDiff:
                return False
            foundDiff = True
            if (len(s1) == len(s2)):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True

if __name__=="__main__":
    if len(sys.argv)<3:
        print("Strings not read...")
    else:
        str1 = str(sys.argv[1])
        str2 = str(sys.argv[2])
        if (abs(len(str1)-len(str2)) > 1):
            print(False)
        else:
            print(oneWay(str1, str2))