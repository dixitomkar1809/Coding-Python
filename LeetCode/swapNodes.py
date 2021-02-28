# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        start = head
        for _ in range(k-1):
            start = start.next
        end = head
        tempEnd = start
        while tempEnd.next:
            end = end.next
            tempEnd = tempEnd.next
        start.val, end.val = end.val, start.val
        return head