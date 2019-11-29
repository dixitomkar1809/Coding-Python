# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    l1: sorted List(List Node)
    l2: sorted List(List Node)
    return : merge of l1 and l2 (List Node)
    """
    def __init__(self, l1, l2):
        self.mergeTwoList(l1, l2)

    def mergeTwoList(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        head1 = l1
        head2 = l2
        head = None
        if (head1.val < head2.val):
            head = head1
            head1 = head1.next
        else :
            head = head2
            head2 = head2.next
        result = head
        while head1 and head2:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else :
                head.next = head2
                head2 = head2.next
            head = head.next
        while head1:
            head.next = head1
            head1 = head1.next
            head = head.next
        while head2:
            head.next = head2
            head2 = head2.next
            head = head.next
        self.displayList(result)
        return result

    def displayList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next

if __name__=="__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l2 = ListNode(3)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    Solution(l1, l2)