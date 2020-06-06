# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B.Each number in A may only be used once in the combination.
'''

# Time Complexity: O(2^n)

class Solution:
    def __init__(self):
        self.results = []

    def getCombination(self, arr, target):
        if target:
            arr.sort()
            self.__getCombinationHelper(arr, 0, [], target)
            return self.results
        return []
    
    def __getCombinationHelper(self, arr, start, path, target):
        if not target:
            self.results.append(path)
            return
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break
            self.__getCombinationHelper(arr, i+1, path+[arr[i]], target-arr[i])

if __name__=='__main__':
    A = [10,1,2,7,6,1,5]
    B = 8
    sol = Solution()
    print(sol.getCombination(A, B))
        