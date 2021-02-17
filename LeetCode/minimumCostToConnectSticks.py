# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/

# Time Complexity: O(nLogn) n is number of sticks

import heapq
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks) == 1:
            return 0
        heapq.heapify(sticks)
        totalCosts = 0
        while len(sticks) != 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            cost = stick1 + stick2
            totalCosts += cost
            heapq.heappush(sticks, cost)
        return totalCosts