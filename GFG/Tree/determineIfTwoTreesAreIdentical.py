# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two binary trees, the task is to find if both of them are identical or not. 
'''

# Time Complexity: O(n) n < m

class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def isIdentical(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            return (root1.value == root2.value and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right))

if __name__=='__main__':
    sol = Solution()
    one = BTreeNode(1)
    two = BTreeNode(2)
    three = BTreeNode(4)
    one.left = two
    one.right = three
    newOne = BTreeNode(1)
    newTwo = BTreeNode(2)
    newThree = BTreeNode(3)
    newOne.left = newTwo
    newOne.right = newThree
    print(sol.isIdentical(one, newOne))