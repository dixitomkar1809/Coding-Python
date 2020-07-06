# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e you have to iterate on the original array only.
'''

# Time Complexity: O(n)

class Solution:
    def zigZag(self, arr):
        flag = True
        for i in range(len(arr)-1):
            if flag:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = not flag
        return arr

if __name__=='__main__':
    sol = Solution()
    print(sol.zigZag([4, 3, 7, 8, 6, 2, 1]))
    print(sol.zigZag([1, 4, 3, 2]))