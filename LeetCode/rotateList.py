# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/rotate-list/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if k == 0:
            return head
        n = 1
        last = head
        while last.next:
            n += 1
            last = last.next
        last.next = head
        newLast = head
        k %= n
        for _ in range(n-k-1):
            newLast = newLast.next
        newHead = newLast.next
        newLast.next = None
        return newHead
        
        
        
            
        
        
        
        
            
        