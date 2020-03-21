# Author: Omkar Dixit
# Email: omedxt@gmail.com

"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tac t Coa
Output: Tru e (permutations : "tac o cat" , "atc o eta" , etc. ) 
"""

# Note please in the terminal use "" if you have spaces in the phrase
# Time Complexity = O(n), we traverse the phrase just once
import sys

def palindromePermutation(phrase):
    hMap = {}
    oddCount = 0
    for char in phrase.strip():
        if char in hMap:
            hMap[char] = hMap[char] + 1
        else:
            hMap[char] = 1
        if hMap[char] % 2 == 1:
            oddCount+=1
        else:
            oddCount-=1
    print(hMap)
    return oddCount == 1 or oddCount == 0

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Phrase Not Detected")
    else:
        print(sys.argv[1])
        print(palindromePermutation(sys.argv[1].replace(" ", "").lower()))