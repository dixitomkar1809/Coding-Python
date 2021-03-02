# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/high-five/

# Time Complexity: O(nLogn) n is number of items

import collections
import heapq

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        hashmap = collections.defaultdict(list)
        for item in items:
            if item[0] not in hashmap:
                hashmap[item[0]].append(item[1])
            else:
                heapq.heappush(hashmap[item[0]], item[1])
            if len(hashmap[item[0]]) > 5:
                heapq.heappop(hashmap[item[0]])
        print(hashmap)
        return [[item, sum(hashmap[item])/5] for item in hashmap]
            
        