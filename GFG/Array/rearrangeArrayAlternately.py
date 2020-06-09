# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on...
'''

class Solution:
    def rearrangeArrayAlternately(self, arr):
        maxIndex = len(arr)-1
        minIndex = 0
        maxElement = arr[-1] + 1
        for i in range(len(arr)):
            if i%2==0:
                arr[i] += (arr[maxIndex] % maxElement) * maxElement
                maxIndex -= 1
            else:
                arr[i] += (arr[minIndex] % maxElement) * maxElement
                minIndex += 1
        for i in range(len(arr)):
            arr[i] = arr[i] // maxElement
        return arr

if __name__=='__main__':
    arr = [1,2,3,4,5,6]
    sol = Solution()
    print(sol.rearrangeArrayAlternately(arr))