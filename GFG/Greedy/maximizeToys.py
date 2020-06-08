# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array consisting cost of toys. Given an integer K depicting the amount with you. Maximise the number of toys you can have with K amount.
'''

# Time Complexity: O(nlogn)

class Solution:
    def maximizeToys(self, arr, k):
        arr.sort()
        summ = 0
        count = 0
        for i in range(len(arr)):
            if summ + arr[i] <= k:
                summ += arr[i]
                count += 1
            else:
                break
        return count
    
if __name__=='__main__':
    arr = [1, 12, 5, 111, 200, 1000, 10, 9, 12, 15] 
    k = 50
    sol = Solution()
    print(sol.maximizeToys(arr, k))
