# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
Output: {2, 1, 3}, {2, 3, 1}
'''

from Node import TreeNode

class Solution:
    def weavedLists(self, first, second, results, prefix):
        if len(first) == 0 or len(second) == 0:
            result = prefix.copy()
            for item in first:
                result.append(item)
            for item in second:
                result.append(item)
            results.append(result)
            return results
        # Remove top from first add to prefix weave first and second again
        headFirst = first.pop(0)
        prefix.append(headFirst)
        self.weavedLists(first, second, results, prefix)
        first.insert(0, prefix.pop(-1))
        # Remove top from second add to prefix weave first and second again
        headSecond = second.pop(0)
        prefix.append(headSecond)
        self.weavedLists(first, second, results, prefix)
        second.insert(0, prefix.pop(-1))

    def allSequences(self, node):
        result = []
        if not node:
            result.append([])
            return result
        prefix = []
        prefix.append(node.value)
        leftSeq = self.allSequences(node.left)
        rightSeq = self.allSequences(node.right)
        for first in leftSeq:
            for second in rightSeq:
                weaved = []
                self.weavedLists(first , second, weaved, prefix)
                for item in weaved:
                    result.append(item)
        return result

if __name__=="__main__":
    fifty = TreeNode(50)
    twenty = TreeNode(20)
    sixty = TreeNode(60)
    ten = TreeNode(10)
    twentyFive = TreeNode(25)
    seventy = TreeNode(70)
    five = TreeNode(5)
    fifteen = TreeNode(15)
    sixtyFive = TreeNode(65)
    eighty = TreeNode(80)
    fifty.left = twenty
    fifty.right = sixty
    twenty.left = ten
    twenty.right = twentyFive
    sixty.right = seventy
    ten.left = five
    ten.right = fifteen
    seventy.left = sixtyFive
    seventy.right = eighty
    five = TreeNode(5)
    four = TreeNode(4)
    one = TreeNode(1)
    seven = TreeNode(7)
    six = TreeNode(6)
    ten = TreeNode(10)
    sol = Solution()
    print(sol.allSequences(fifty))
    