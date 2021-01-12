# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball, {"at",
""}
Output: 4
'''

# Time Complexity: O(n)

def solution(strs, searchTerm, first, last):
    if (first > last):
        return -1
    mid = (first + last) // 2
    if strs[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < first and right > right:
                return -1
            elif left >= first and strs[left] != "":
                mid = left
                break
            elif right <= last and strs[right] != "":
                mid = right
                break
            left -= 1
            right += 1
    if strs[mid] == searchTerm:
        return mid
    elif sorted([strs[mid], searchTerm])[0] == strs[mid]:
        return solution(strs, searchTerm, mid + 1, last)
    else:
        return solution(strs, searchTerm, first, mid - 1)

if __name__=="__main__":
    strs = ["at","", "", "", "", "ball", "", "", "car", "", "", "dad", ""]
    print(solution(strs, 'dad', 0, 12))