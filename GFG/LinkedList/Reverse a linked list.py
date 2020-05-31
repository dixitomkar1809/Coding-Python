# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a linked list of N nodes. The task is to reverse this list.

Input: Head of following linked list
1->2->3->4->NULL
Output: Linked list should be changed to,
4->3->2->1->NULL

Input: Head of following linked list
1->2->3->4->5->NULL
Output: Linked list should be changed to,
5->4->3->2->1->NULL

Input: 1->NULL
Output: 1->NULL

Input:
The first line of input contains the number of test cases T. For each test case, the first line contains the length of the linked list and the next line contains the elements of the linked list.

Output:
For each test case, print the reversed linked list in a new line.

User Task:
The task is to complete the function reverseList() with head reference as the only argument and should return new head after reversing the list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 104

Example:
Input:
2
6
1 2 3 4 5 6
5
2 7 8 9 10
Output:
6 5 4 3 2 1
10 9 8 7 2
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse(self, root):
        next = prev = None
        curr = root
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def printList(self, root):
        curr = root
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    sol = Solution()
    newHead = sol.reverse(head)
    sol.printList(newHead)