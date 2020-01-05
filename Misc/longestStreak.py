# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Returns longest streak of consecutive integers in an array (Unsorted)
# TC - O(n)

def longestStreak(arr):
    hashMap = {}
    ans = 0
    for item in arr:
        hashMap[item] = 0
    for i in range(len(arr)):
        if arr[i] - 1 not in hashMap:
            j = arr[i]
            while j in hashMap:
                j += 1
            ans = max(ans, j - arr[i])
    return ans

if __name__=="__main__":
    arr = [1,9,3,10,4,20,2]
    print(longestStreak(arr))