# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/sort-array-by-parity-ii/

# Time Complexity: O(N)

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(A)):
            if i % 2 == 0:
                A[i] = even.pop()
            else:
                A[i] = odd.pop()
        return A