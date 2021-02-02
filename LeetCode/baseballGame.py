# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/baseball-game/

# Time Complexity: O(n)

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for i, op in enumerate(ops):
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(scores[-1] * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
        