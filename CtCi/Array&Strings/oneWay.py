# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

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
    if len(str1) > len(str2):
        if len(Counter(str1)-Counter(str2))==1:
            return True
        return False
    else:
        if len(Counter(str2)-Counter(str1))==1:
            return True
        return False

if __name__=="__main__":
    if len(sys.argv)<3:
        print("Strings not read...")
    else:
        str1 = str(sys.argv[1])
        str2 = str(sys.argv[2])
        print(oneWay(str1, str2))