# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree, find its height.
'''

# Time Complexity: O(logn)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def height(self, node):
        if not node: return 0
        return 1 + max(self.height(node.left), self.height(node.right))

if __name__=='__main__':
    sol = Solution()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.left = two
    two.right = three
    print(sol.height(one))