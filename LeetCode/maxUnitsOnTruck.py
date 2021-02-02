# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/maximum-units-on-a-truck/

# Time Complexity: O(nLogn)

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes = sorted(boxTypes, reverse=True, key=lambda x:x[1])
        for boxq, units in boxTypes:
            if truckSize - boxq >= 0:
                res += ((boxq) * units)
                truckSize -= boxq
            else:
                res += ((truckSize) * units)
                break
        return res