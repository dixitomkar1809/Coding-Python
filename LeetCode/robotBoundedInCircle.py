# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/robot-bounded-in-circle/

# Time Complexity: O(n)

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        index = 0
        x = 0
        y = 0
        for i in instructions:
            if i == 'L':
                index = (index + 3) % 4
            elif i == 'R':
                index = (index + 1) % 4
            else:
                x += directions[index][0]
                y += directions[index][1]
        return (x == 0 and y == 0) or index != 0