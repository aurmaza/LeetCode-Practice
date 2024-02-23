# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right and isLeft:
                return node.val
            if not node.left and not node.right and not isLeft:
                return 0
            left = helper(node.left, True)
            right = helper(node.right, False)
            return left + right
        return helper(root, False)
