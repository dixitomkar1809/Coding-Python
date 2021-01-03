# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''

# Time Complexity: O(n)

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
        