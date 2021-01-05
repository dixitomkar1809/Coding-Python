# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.
'''


# Time Complexity: O(y) 
def mulitply1(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + mulitply1(x, y-1)
    if y < 0:
        return - mulitply1(x, -y)


#   Time Complexity: O (log (x)) when x is smaller than y
def mulitply2(x, y):
    smaller = x if x < y else y
    bigger = x if x > y else y
    return multiplyHelper(smaller, bigger)

def multiplyHelper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    else:
        small = smaller // 2
        halfProd = multiplyHelper(small, bigger)
        if smaller % 2 == 0:
            return halfProd + halfProd
        else:
            return halfProd + halfProd + bigger    
    
    
if __name__== "__main__":
    print(mulitply1(5, 5))
    print(mulitply2(5, 5))