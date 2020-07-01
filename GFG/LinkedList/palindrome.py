# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
'''

# Time Complexity: O(n)

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def palindrome(self, head):
        if not head:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = next = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

if __name__=='__main__':
    sol = Solution()
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    print(sol.palindrome(head))