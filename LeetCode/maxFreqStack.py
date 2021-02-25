# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/maximum-frequency-stack/

# Time Complexity: O(1)

import collections
import heapq

class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxFreq = 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        freq = self.freq[x] + 1
        self.freq[x] = freq
        if freq > self.maxFreq:
            self.maxFreq = freq
        self.group[freq].append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.maxFreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return x
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
