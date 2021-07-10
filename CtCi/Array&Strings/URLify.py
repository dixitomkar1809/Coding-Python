# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

import sys

# Time Complexity O(n)

def URLify(str):
    return "%20".join(str)

if __name__=="__main__":
    if len(sys.argv)==1:
        print("String Not Detected")
    else:
        print(URLify(sys.argv[1:]))