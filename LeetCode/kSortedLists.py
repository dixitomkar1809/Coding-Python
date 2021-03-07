# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/merge-k-sorted-lists/

# Time Complexity: O(nlogk) n is number of elements in a list, k is number of lists

import collections
import heapq


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class mergeLLNode:
    def __init__(self, listIndex, currNode):
        self.listIndex = listIndex
        self.currNode = currNode
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        curr = None
        if not lists:
            return None
        if len(lists) == 1:
            if not lists[0]:
                return None
            else:
                return lists[0]
        pq = []
        for i, item in enumerate(lists):
            if item:
                pq.append((item.val, mergeLLNode(i, item)))
        heapq.heapify(pq)
        while pq:
            val, mergeLLNodeInstance = heapq.heappop(pq)
            if not head:
                head = ListNode(val)
                curr = head
            else:
                curr.next = ListNode(val)
                curr = curr.next
            if mergeLLNodeInstance.currNode.next:
                mergeLLNodeInstance.currNode = mergeLLNodeInstance.currNode.next
                pq.append((mergeLLNodeInstance.currNode.val, mergeLLNode(mergeLLNodeInstance.listIndex, mergeLLNodeInstance.currNode)))
                heapq.heapify(pq)
        return head