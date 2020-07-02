# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to tree and returns it.
'''

class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None

class Solution:
    def serialize(self, root):
        if not root:
            return []
        return self.__serializeDFS(root, [])

    def deserialize(self, arr):
        if not arr: return None
        return self.__deserializeHelper(arr)

    def __serializeDFS(self, root, arr):
        if not root:
            arr.append(None)
        else:
            arr.append(root.data)
            arr = self.__serializeDFS(root.left, arr)
            arr = self.__serializeDFS(root.right, arr)
        return arr
    
    def __deserializeHelper(self, arr):
        if not arr[0]:
            arr.pop(0)
            return None
        root = Node(arr.pop(0))
        root.left = self.__deserializeHelper(arr)
        root.right = self.__deserializeHelper(arr)
        return root

if __name__=='__main__':
    sol = Solution()
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.right.left = Node(4)
    root.right.right = Node(5)
    arr = sol.serialize(root)
    newRoot = sol.deserialize(arr)
