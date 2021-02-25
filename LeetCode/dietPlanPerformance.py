# Link: https://leetcode.com/problems/diet-plan-performance/

# Time Complexity: O(N) N is number of elements in array

class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        points = 0
        s = sum(calories[:k])
        if s < lower:
            points -= 1
        if s > upper:
            points += 1
        for i in range(k, len(calories)):
            s += (-calories[i-k] + calories[i])
            if s < lower:
                points -= 1
            if s > upper:
                points += 1
        return points