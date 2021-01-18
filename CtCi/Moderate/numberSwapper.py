# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Number Swapper: Write a function to swap a number in place (that is, without temporary variables).
'''

def solution(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__=="__main__":
    print(solution(9, 4))
