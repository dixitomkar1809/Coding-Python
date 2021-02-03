# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i
        return None
