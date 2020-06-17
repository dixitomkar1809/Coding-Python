# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of integers. Find the minimum number of swaps required to sort the array in non-decreasing order.
'''

# Time Complexity: O(nLogn)

class Solution:
    def minSwapsToSort(self, arr):
        posVal = [*enumerate(arr)]
        posVal.sort(key=lambda x:x[1])
        visited = [False] * len(arr)
        swaps = 0
        for i in range(len(arr)):
            if visited[i] or posVal[i][0] == i:
                continue
            cycleSize = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = posVal[j][0]
                cycleSize += 1
            if cycleSize > 0:
                swaps += (cycleSize -1)
        return swaps

if __name__=='__main__':
    sol  = Solution()
    arr = [4,3,2,1]
    print(sol.minSwapsToSort(arr))
    arr = [1,4,3,2]
    print(sol.minSwapsToSort(arr))
    arr = [1,5,4,3,2]
    print(sol.minSwapsToSort(arr))