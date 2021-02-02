# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/merge-two-sorted-lists/

# Time Complexity: O(n + m)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        curr = None
        if l1.val <= l2.val:
            curr = l1
            l1 = l1.next
        else:
            curr = l2
            l2 = l2.next
        head = curr
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        return head
        
        