# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
'''

# Time Complexity: O(n^2)

class Solution:
    def pythagoreanTriplet(self, arr):
        for i in range(len(arr)):
            arr[i] = arr[i] * arr[i]
        arr.sort()
        for i in range(len(arr)-1, 1, -1):
            j = 0
            k = i - 1
            while j < k:
                if arr[j] + arr[k] == arr[i]:
                    return True
                else:
                    if arr[j] + arr[k] < arr[i]:
                        j += 1
                    else:
                        k -= 1
        return False

if __name__=='__main__':
    sol = Solution()
    print(sol.pythagoreanTriplet([3, 1, 4, 6, 5]))