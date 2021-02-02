# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/copy-list-with-random-pointer/

# Time Complexity: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.nodes = {}
        if not head:
            return head
        oldnode = head
        newnode = Node(oldnode.val, oldnode.next)
        self.nodes[oldnode] = newnode
        while oldnode:
            newnode.next = self.getClone(oldnode.next)
            newnode.random = self.getClone(oldnode.random)
            oldnode = oldnode.next
            newnode = newnode.next
        return self.nodes[head]
            
    def getClone(self, node):
        if node: 
            if node not in self.nodes:
                self.nodes[node] = Node(node.val, node.next)
            return self.nodes[node]
        return None
    
                