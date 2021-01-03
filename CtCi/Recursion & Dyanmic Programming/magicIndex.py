# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Magic Index: A magic index in an array A[ 1 .•. n-1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
'''

# Time Complexity: O(logn)
# Doesnt work when the array has duplicates
def solutionSlow(arr, left, right):
    if (right < left):
        return -1
    mid = (left + right) // 2
    if arr[mid] == mid :
        return mid
    elif arr[mid] > mid:
        return solutionSlow(arr, left, mid)
    else:
        return solutionSlow(arr, mid + 1, right)


# Time Complexity: O(logn)
def solutionFast(arr, left, right):
    if right < left:
        return -1
    midIndex = (left + right) // 2
    midValue = arr[midIndex]
    
    if (midIndex == midValue):
        return midIndex
    leftIndex = min(midIndex - 1, midValue)
    left = solutionFast(arr, left, leftIndex)
    if left >= 0:
        return left
    rightIndex = max(midIndex + 1, midValue)
    right = solutionFast(arr, rightIndex, right)
    return right
        
if __name__ == '__main__':
    arr = [-40, -20, 2, 2, 2, 3, 5, 6, 8, 12, 13]
    print(solutionSlow(arr, 0, len(arr)-1))
    print(solutionFast(arr, 0, len(arr)-1))