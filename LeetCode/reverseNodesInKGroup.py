# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Time Complexity: O(n) n is number of nodes in ll

import collections
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count == k:
            newHead = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(curr, k)
            return newHead
        return head
    
    
    def reverseLinkedList(self, head, k):
        curr = head
        prev = None
        while curr and k != 0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            k -= 1
        return prev