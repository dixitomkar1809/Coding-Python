# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/count-number-of-teams/

# Time Complexity: O(n^2) n is number of ratings

import collections
import heapq

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        cnt = 0
        for j in range(1, len(rating)):
            x, lowLeft, highLeft, lowRight, highRight = rating[j], 0, 0, 0, 0
            for i in range(j):
                if rating[i] < x:
                    lowLeft += 1
                else:
                    highLeft += 1
            for k in range(j+1, len(rating)):
                if rating[k] < x:
                    lowRight += 1
                else:
                    highRight += 1
            cnt += ((lowLeft * highRight) + (highLeft * lowRight))
        return cnt