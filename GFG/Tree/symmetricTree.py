# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.
'''

# Time Complexity: O(n) 

class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            return (root1.value == root2.value and self.isSymmetric(root1.left, root2.right) and self.isSymmetric(root1.right, root2.left))

if __name__=='__main__':
    sol = Solution()
    one = BTreeNode(1)
    two = BTreeNode(2)
    three = BTreeNode(3)
    four = BTreeNode(4)
    newTwo = BTreeNode(2)
    newThree = BTreeNode(3)
    newFour = BTreeNode(9)
    one.left = two
    one.right = newTwo
    two.left = three
    two.right = four
    newTwo.left = newFour
    newTwo.right = newThree
    print(sol.isSymmetric(one.left, one.right))