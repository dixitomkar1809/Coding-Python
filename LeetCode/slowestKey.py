# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/slowest-key/

# Time Complexity: O(n)

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxInterval = releaseTimes[0]
        key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i-1] > maxInterval:
                maxInterval = releaseTimes[i] - releaseTimes[i-1]
                key = keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i-1] == maxInterval and keysPressed[i] > key:
                maxInterval = releaseTimes[i] - releaseTimes[i-1]
                key = keysPressed[i]
        return key
        