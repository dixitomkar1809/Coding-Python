# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/relative-sort-array/

# Time Complexity: O(n * m) n is items in arr1 and m is items in arr2
import collections

class Solution:
    def relativeSortArray(self, arr1, arr2):
        hashmap = collections.defaultdict(int)
        for i, element in enumerate(arr1):
            hashmap[element] += 1
        sol = []
        for i, element in enumerate(arr2):
            for j in range(hashmap[element]):
                sol.append(element)
            del hashmap[element]
        remaining = sorted(hashmap.keys())
        for element in remaining:
            for j in range(hashmap[element]):
                sol.append(element)
            del hashmap[element]
        return sol