# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/top-k-frequent-words/

# Time Complexity: O(N + klogN)

import heapq, collections
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap = []
        counts = collections.Counter(words)
        for word in counts:
            heap.append((-counts[word], word))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
                
        