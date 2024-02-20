# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        temp = []
        def helper(node, currSum):
            if not node:
                return
            stringVal = str(node.val)
            if not node.left and  not node.right:
                temp.append(currSum + stringVal)
                return 
            helper(node.left, currSum + stringVal)
            helper(node.right, currSum + stringVal)
        helper(root, '')
        res = [int(n, 2) for n in temp]
        return sum(res)
