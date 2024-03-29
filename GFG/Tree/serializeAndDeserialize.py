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
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        return self.serializeHelper(root, '')
    
    def serializeHelper(self, root, data):
        if root is None:
            data += 'None,'
        else:
            data += (str(root.val) + ',')
            data = self.serializeHelper(root.left, data)
            data = self.serializeHelper(root.right, data)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        dataList = data.split(',')
        return self.deserializeHelper(dataList)
    
    def deserializeHelper(self, data):
        if data[0] == 'None':
            data.pop(0)
            return None
        root = Node(data.pop(0))
        root.left = self.deserializeHelper(data)
        root.right = self.deserializeHelper(data)
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
