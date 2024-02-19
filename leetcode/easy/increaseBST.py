# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def getInOrder(root, res):
            if not root:
                return
            getInOrder(root.left, res)
            res.append(root.val)
            getInOrder(root.right,res)
            return res
        
        
        def createTree(arr, index):
            if index >= len(arr):
                return 
            print(arr,index)
            root = TreeNode(val = arr[index])
            index+=1
            root.right = createTree(arr, index)
            return root
        
        inOrderArr = getInOrder(root, [])
        res = createTree(inOrderArr, 0)
        return res
