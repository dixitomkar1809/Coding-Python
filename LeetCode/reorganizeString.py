# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reorganize-string/

# Time Complexity: O(nlogk) mostly O(n) since k would be 26

import collections, heapq

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counts = collections.Counter(S)
        pq = []
        for char in counts:
            pq.append((-counts[char], char))
        heapq.heapify(pq)
        if -(pq[0][0]) > (len(S) + 1)/2:
            return ''
        sol = ''
        print(pq)
        while len(pq) >= 2:
            count1, char1 = heapq.heappop(pq)
            count2, char2 = heapq.heappop(pq)
            sol += (char1 + char2)
            if count1 + 1 != 0:
                heapq.heappush(pq, (count1 + 1, char1))
            if count2 + 1 != 0:
                heapq.heappush(pq, (count2 + 1, char2))
        if pq:
            sol += pq[0][1]
        return sol
        