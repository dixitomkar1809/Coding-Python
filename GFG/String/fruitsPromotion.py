# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana

Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output
Return an integer 1 if the customer is a winner else return 0.

Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

Example 2:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

Example 3:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.

Example 4:

Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.
'''
    
# Time Complexity: O(M+N) M is lenght of pattern, N is length of main string 

def solution(listOfFruits, listOfListFruitPattern):
    for pattern in listOfListFruitPattern:
        print(solutionHelper(listOfFruits, pattern))
    
def solutionHelper(mainString, pattern):
    lps = generateLSA(pattern)
    i = 0
    j = 0
    solution = []
    while i < len(mainString):
        if mainString[i] == pattern[j] or pattern[j] == '*':
            i += 1
            j += 1
        if j == len(pattern):
            solution.append(i-j)
            j = lps[j-1]
        elif i < len(mainString) and mainString[i] != pattern[j] and pattern[j] != '*':
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return solution
    
def generateLSA(pattern):
    lps = [0] * len(pattern)
    prefixLength = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prefixLength] or pattern[i] == '*' or pattern[prefixLength] == '*':
            prefixLength += 1
            lps[i] = prefixLength
            i += 1
        else:
            if prefixLength != 0:
                prefixLength = lps[prefixLength - 1]
            else:
                i += 1
    return lps

if __name__=="__main__":
    solution(['orange', 'apple', 'apple', 'banana', 'orange', 'banana'], [['apple', 'apple'], ['banana', '*', 'banana']])