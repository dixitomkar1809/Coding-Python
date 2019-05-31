# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head =l1
        while l2:
            summ = l2.val + l1.val + carry
            l1.val = summ % 10
            carry = summ //10
            if not l1.next:
                l1.next = l2.next
                break
            if not l2.next:
                break
            l1 = l1.next
            l2 = l2.next
        while carry > 0:
            if not l1.next:
                l1.next =  ListNode(0)
            l1 = l1.next
            summ = carry + l1.val
            l1.val = summ % 10
            carry  = summ //10
        return head
        
        