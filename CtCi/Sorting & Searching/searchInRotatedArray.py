# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
lnput:find5in{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
'''

# Time Complexity: O(logn)

def solution(arr, x):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if (arr[mid] == x):
            return mid
        elif arr[left] < arr[mid]:
            if x >= arr[left] and x < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if x < arr[left] and x > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
        
if __name__ == '__main__':
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    # x = 5
    x = 3
    # x = 1
    print(solution(arr, x))