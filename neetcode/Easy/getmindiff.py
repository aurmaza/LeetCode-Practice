# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        currMin = float('inf')
        temp = []
        def helper(root):
            nonlocal temp
            if not root:
                return
            helper(root.left)
            temp.append(root.val)
            helper(root.right)
        helper(root)
        
        for i in range(len(temp)-1):
            currMin = min(currMin, abs(temp[i]-temp[i+1]))
        return currMin


        
