# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

# Time Complexity: O(n) n is number of elements in the postfix

import collections
import heapq

import abc 
from abc import ABCMeta, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node:
    __metaclass__ = ABCMeta
    # define your fields here
    @abstractmethod
    def evaluate(self):
        pass


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def evaluate(self):
        if self.value in ['+', '-', '*', '/']:
            left = self.left.evaluate()
            right = self.right.evaluate()
            if self.value == '+':
                return left + right
            elif self.value ==  '-':
                return left - right
            elif self.value == '*':
                return left * right
            else:
                return left // right
        else:
            return self.value
class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: int
        """
        nums = []
        item = postfix.pop()
        root = None
        if item in ['+', '-', '*', '/']:
            root = TreeNode(item)
            root.right = self.buildTree(postfix)
            root.left = self.buildTree(postfix)
        else:
            root = TreeNode(int(item))
            return root
        return root
        
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        