# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Group Anagrams: Write a method to sort an array ot strings so that all tne anagrnms are next to
each other.
'''

# Time Complexity: O(n * m) n -> number of items, m -> number of chars in word

from collections import defaultdict
def solution(strs):
    if strs == []:
        return []
    if len(strs) == 1:
        return [strs[0]]
    sol = defaultdict(list)
    for item in strs:
        count = [0] * 26
        for char in item:
            count[ord(char) - ord('a')] += 1
        sol[tuple(count)].append(item)
    return list(sol.values())



if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(solution(strs))
