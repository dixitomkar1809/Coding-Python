# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
'''

import sys
from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal


def sortedArrayToBST(arr):
    if not arr :
        return None
    mid = len(arr)//2
    root = TreeNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

if __name__=="__main__":
    arr = []
    for x in sys.argv[1:]:
        arr.append(int(x))
    preOrderTraversal(sortedArrayToBST(arr))