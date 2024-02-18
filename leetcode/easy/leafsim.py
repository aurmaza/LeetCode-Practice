# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(root, temp):
            if not root:
                return
            if not root.left and not root.right:
                temp.append(root.val)
            
            helper(root.left, temp)
            helper(root.right, temp)
            return temp
        # print(helper(root1),helper(root2))
        return helper(root1, []) == helper(root2, [])
    
