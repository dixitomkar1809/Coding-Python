# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given two arrays, A and B, of equal size N. The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.
'''

# Time Complexity: O(nLogn)

class Solution:
    def minSumOfProduct(self, arr1, arr2):
        arr1.sort()
        arr2.sort()
        output = 0
        for i in range(len(arr1)):
            output += (arr1[i] * arr2[len(arr1)-i-1])
        return output

if __name__=='__main__':
    sol = Solution()
    print(sol.minSumOfProduct([3, 1, 1], [6, 5, 4]))
    print(sol.minSumOfProduct([6, 1, 9, 5, 4], [3, 4, 8, 2, 4]))