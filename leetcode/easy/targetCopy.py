# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def helper(node1, node2):
            
            if node1:
                print(node1.val,node2.val)
                if node1 == target:
                    return node2
                left = helper(node1.left, node2.left)
                right = helper(node1.right,node2.right)
                return left or right
            
        
        return helper(original, cloned)
            
