# Author: Omkar Dixit
# Email: omedxt@gmail.com

#  Rod Cutting

# Time Complexity: O(n^2)

import sys

def rodCutting(n, prices):
    R = [0] * (n+1)
    for k in range(1, n+1):
        q = float('-inf')
        for i in range(k):
            q = max(q, prices[i]+R[k-i-1])
        R[k] = q
    return R[-1]


if __name__=="__main__":
    prices = [0,1,5,8,9,10,17,17,20,24,30]
    print(rodCutting(len(prices), prices))