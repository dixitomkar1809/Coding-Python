# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree, connect the nodes that are at same level.Structure of the given Binary Tree node is like following.

struct Node
{
      int data;
      Node* left;
      Node* right;
      Node* nextRight;
}
Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
       10                          10 ------> NULL
      / \                       /      \
     3   5       =>           3 ------> 5 --------> NULL
    / \   \                  \           \
   4   1   2               4 --> 1 -------> 2 -------> NULL
'''

from collections import defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.nextRight = None
        self.left = None
        self.right = None

# Time Complexity: O(n) 

class Solution:
    def connectNodesAtSameLevel(self, root):
        queue = [(root, 0)]
        levelOrderTraversal = defaultdict(list)
        while queue:
            node, level = queue.pop(0)
            levelOrderTraversal[level].append(node)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        levelOrderTraversal = list(levelOrderTraversal.values())
        for i in range(len(levelOrderTraversal)):
            if len(levelOrderTraversal[i]) > 1:
                nodes = levelOrderTraversal[i]
                for j in range(len(nodes)):
                    if j+1 < len(nodes):
                        nodes[j].nextRight = nodes[j+1]

if __name__=='__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    one.left = two
    one.right = three
    two.left = seven
    two.right = six
    three.left = five
    three.right = four
    sol = Solution()
    sol.connectNodesAtSameLevel(one)

