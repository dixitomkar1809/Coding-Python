# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
Outp
'''

def solution(n):
    memo = [-1] * (n + 2)
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i -2] + memo[i-3]
    return memo[n]
        
if __name__ == '__main__':
    n = 4
    print(solution(n))
        