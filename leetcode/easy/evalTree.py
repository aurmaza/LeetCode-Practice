# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, r: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root.left and not root.right:                
                return root.val
            left = helper(root.left)
            right = helper(root.right)
            evl = root.val
            if evl == 2:
                return left or right
            if evl == 3:
                return left and right
        return helper(r)
