
# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Time Complexity: O(N) n is number of nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        stack = [[root, 0]]
        while stack:
            root, currNumber = stack.pop()
            if root:
                currNumber = (currNumber <<  1) | root.val
                if root.left is None and root.right is None:
                    ans += currNumber
                else:
                    stack.append([root.right, currNumber])
                    stack.append([root.left, currNumber])
        return ans 