# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Problem:  https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Time Complexity: O(n)

import collections

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        hashmap = collections.defaultdict(int)
        count = 0
        for t in time:
            if t % 60  == 0:
                count += hashmap[0]
            else:
                count += hashmap[(60-t%60)]
            hashmap[t%60] += 1
        return count