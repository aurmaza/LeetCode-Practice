# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkBalance(root):
            
            if root is None:
                return 0
            left = checkBalance(root.left)
            right = checkBalance(root.right)
            dif = abs(left-right)
            if dif > 1 or left == -1 or right == -1:
                return -1
            return max(left, right) + 1
        res = checkBalance(root)
        if res  == -1:
            return False
        return True
