# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.totalPaths = 0

    def pathSum(self, root, targetSum):
        cacheMap = {0:1}
        self.dfs(root, targetSum, 0, cacheMap)
        return self.totalPaths

    def dfs(self, root, targetSum, currentSum, cacheMap):
        if not root:
            return 
        currentSum += root.value
        oldPathSum = currentSum - targetSum
        self.totalPaths = cacheMap.get(oldPathSum, 0) + 1
        cacheMap[currentSum] = cacheMap.get(currentSum, 0) + 1
        self.dfs(root.left, targetSum, currentSum, cacheMap)
        self.dfs(root.right, targetSum, currentSum, cacheMap)
        cacheMap[currentSum] -= 1

if __name__=="__main__":
    ten = TreeNode(10)
    five = TreeNode(5)
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    newThree = TreeNode(3)
    minusTwo = TreeNode(-2)
    minusThree = TreeNode(-3)
    eleven = TreeNode(11)
    ten.left = five
    ten.right = minusThree
    minusThree.right = eleven
    five.left = three
    three.left = newThree
    three.right = minusTwo
    five.right = one
    one.right = two
    sol = Solution()
    print(sol.pathSum(ten, 8))