# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
'''

import sys

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if not arr :
        return None
    mid = len(arr)//2
    root = BSTNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

def preOrder(root): 
    if not root: 
        return
    print(root.value) 
    preOrder(root.left) 
    preOrder(root.right) 

if __name__=="__main__":
    arr = []
    for x in sys.argv[1:]:
        arr.append(int(x))
    preOrder(sortedArrayToBST(arr))
    
