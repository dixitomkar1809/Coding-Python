# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
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