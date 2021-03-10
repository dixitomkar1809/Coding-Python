# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1
'''

# Time Complexity: O(n ^ 2) n is number of elements in array

import collections

class Solution:
    def solution(self, arr):
        hashmap = collections.defaultdict(int)
        sol = collections.defaultdict()
        for item in arr:
            hashmap[item] = 0
        for item in arr:
            for secondItem in hashmap:
                if item != secondItem:
                    if (item + secondItem) in hashmap:
                        if item < secondItem:
                            sol[(item, secondItem)] = 0
                        else:
                            sol[(secondItem, item)] = 0
        return len(sol.keys())
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.solution([1,5,3,2]))
    print(solution.solution([2,3,4]))
            