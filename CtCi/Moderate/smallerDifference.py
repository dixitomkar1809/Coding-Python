# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference.
EXAMPLE
Input: {l, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
Output: 3. That is, the pair (11, 8).
'''

# Time Complexity: O(nlogn + mlogm)

def solution(input1, input2):
    input1.sort()
    input2.sort()
    p1 = 0
    p2 = 0
    minDifference = float('inf')
    while p1 < len(input1) and p2 < len(input2):
        if abs(input1[p1] - input2[p2]) < minDifference:
            minDifference = abs(input1[p1] - input2[p2])
        if input1[p1] < input2[p2]:
            p1 += 1
        else:
            p2 += 1
    return minDifference

if __name__=="__main__":
    print(solution([1, 3, 15, 11, 2], [8, 19, 23, 127]))