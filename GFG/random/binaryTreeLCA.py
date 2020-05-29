# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def findLCA(self, root, n1, n2):
        if not root:
            return None
        
        if root.value == n1.value or root.value == n2.value:
            return root
        
        leftLCA = self.findLCA(root.left, n1, n2)
        rightLCA = self.findLCA(root.right, n1, n2)

        if leftLCA and rightLCA:
            return root

        if leftLCA is not None:
            return leftLCA
        else:
            return rightLCA

if __name__=="__main__":
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    one.left = two
    one.right = three
    two.left = four
    two.right = five 
    three.left = six
    three.right = seven
    sol = Solution()
    print(sol.findLCA(one, four, five).value)
    print(sol.findLCA(one, four, six).value)
    print(sol.findLCA(one, three, four).value)
    print(sol.findLCA(one, two, four).value)