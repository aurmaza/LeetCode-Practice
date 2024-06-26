# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, val):
            if not root:
                return
            print(root.val)
            val += str(root.val)
            if not root.left and not root.right:
                res.append(val)    
            else:
                val+="->"
                dfs(root.left,val)
                dfs(root.right, val)
        dfs(root, "")
        return res

        
