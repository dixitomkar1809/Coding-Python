# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-linked-list-ii/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return None
        curr = head
        prev = None
        while left > 1:
            prev = curr
            curr = curr.next
            left -=  1
            right -= 1
        rightConnection = curr
        leftConnection = prev
        while right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            right -= 1
        if leftConnection:
            leftConnection.next = prev
        else:
            head = prev
        rightConnection.next = curr
        return head