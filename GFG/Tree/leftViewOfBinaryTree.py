# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /   \    /    \
  4     5   6    7
   \
     8
'''

from collections import defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self, root):
        self.root = root
        self.levelOrderTraversal = self.__levelOrderTraversal()
    
    # Time Complexity = O(n)
    def __levelOrderTraversal(self):
        queue = []
        queue.append([self.root, 0])
        levelOrderTraversal = defaultdict(list)
        while queue:
            node, level = queue.pop(0)
            levelOrderTraversal[level].append(node)
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return levelOrderTraversal
    
    # Time Complexity = O(n)
    def leftView(self):
        print("Left View")
        for item in self.levelOrderTraversal.values():
            print(item[0].value, end=" ")
        print()
        return

if __name__=="__main__":
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    one.left = two
    one.right = three
    two.left = four
    two.right = five 
    three.left = six
    three.right = seven
    sol = Solution(one)
    sol.leftView()