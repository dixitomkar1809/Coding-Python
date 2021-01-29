# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
'''

# Time Complexity: O(n)

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