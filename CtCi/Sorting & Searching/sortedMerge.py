# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
'''

#Time Complexity: (O(lastA + lastB))

def solution(A, B, lastA, lastB):
    indexA = lastA - 1
    indexB = lastB - 1
    last = lastB + lastA - 1
    while indexB >= 0:
        if A[indexA] > B[indexB] and indexA >= 0:
            A[last] = A[indexA]
            indexA -= 1
        else:
            A[last] = B[indexB]
            indexB -= 1
        last -= 1
    return A

if __name__ == '__main__':
    print(solution([2,4,6,8,-1,-1,-1], [1,3,9], 4, 3))