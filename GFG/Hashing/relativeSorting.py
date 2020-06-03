# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2, append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
'''

from collections import Counter

class Solution:
    def relativeSorting(self, a1, a2):
        counterA = {}
        missing = []
        output = []
        for item in a2:
            counterA[item] = 0
        for item in a1:
            if item in counterA:
                counterA[item] += 1
            else:
                missing.append(item)
        for item in a2:
            for _ in range(0, counterA[item]):
                output.append(item)
        missing.sort()
        for item in missing:
            output.append(item)
        return output

if __name__=="__main__":
    a1 = [2,1,2,5,7,1,9,3,6,8,8]
    a2 = [2,1,8,3]
    a3 = [2,6,7,5,2,6,8,4]
    a4 = [2,6,4,5]
    sol = Solution()
    print(sol.relativeSorting(a1, a2))
