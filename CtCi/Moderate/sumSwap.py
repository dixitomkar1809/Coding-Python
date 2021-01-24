# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Sum Swap: Given two arrays of integers, find a pair of values (one value from each array) that you
can swap to give the two arrays the same sum.
EXAMPLE
lnput:{4, 1, 2, 1, 1, 2}and{3, 6, 3, 3}
Output: {1, 3}
'''

# Time Complexity: O(m+n) m is len(arr1), n is len(arr2)


def getTarget(arr1, arr2):
    sumA = sum(arr1)
    sumB = sum(arr2)
    if (sumA - sumB) % 2 != 0:
        return None
    return (sumA - sumB) // 2

def solution(arr1, arr2):
    target = getTarget(arr1, arr2)
    if (target is None): return None
    return helper(arr1, arr2, target)

def helper(arr1, arr2, target):
    hmap = {}
    for item in arr2:
        hmap[item] = 1
    for one in arr1:
        two = one - target
        if hmap[two]:
            return one, two
    return None
        
if __name__=="__main__":
    print(solution([4,1,2,1,1,2], [3,6,3,3]))
        