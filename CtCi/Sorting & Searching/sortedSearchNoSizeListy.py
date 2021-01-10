# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
'''

# Time Complexity: O(logn)

def solution(arr, value):
    index = 1
    while elementAt(index, arr) != -1 and elementAt(index, arr) < value:
        index *= 2
    return binarySearch(arr, value, index//2, index)

def elementAt(index, arr):
    if len(arr)-1 < index:
        return -1
    return arr[index]

def binarySearch(arr, value, left, right):
    while left <= right:
        mid = (left + right) // 2
        middle = elementAt(mid, arr)
        if middle == value:
            return mid
        elif middle > value or middle == -1:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    arr = [1,9, 23, 47, 52]
    print(solution(arr, 9))