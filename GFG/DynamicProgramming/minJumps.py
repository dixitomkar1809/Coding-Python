# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of integers where each element represents the max number of steps that can be made forward from that element. The task is to find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.
'''

# Time Complexity: O(n^2)

class Solution:
    def minJumps(self, arr):
        jumps = [0 for _ in range(len(arr))]
        for i in range(1, len(arr)):
            jumps[i] = float('inf')
            for j in range(i):
                if i <= j + arr[j] and jumps[j] != float('inf'):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
        return jumps[-1]

if __name__=='__main__':
    sol = Solution()
    print(sol.minJumps([1, 3, 6, 1, 0, 9]))
    print(sol.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(sol.minJumps([1, 4, 3, 2, 6, 7]))