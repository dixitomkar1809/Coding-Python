# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/asteroid-collision/

# Time Complexity: O(n)

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            asteroid = asteroids[i]
            if asteroid > 0:
                stack.append(asteroid)
            else:
                self.helper(asteroid, stack)
        return stack
    
    
    def helper(self, asteroid, stack):
        while True:
            if stack and stack[-1] > 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] > abs(asteroid):
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)
                break