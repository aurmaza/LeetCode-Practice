# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sameTree(self, s, t):
        # If both trees are empty, return true
        if not s and not t:
            return True
        #If non empty, compare the trees
        if s and t and s.val == t.val:
            #Compare if nodes are the same
            return (self.sameTree(s.left, t.left)) and (self.sameTree(s.right, t.right))
        #One tree is empty, one is non empty, return false
        return False
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        #If the sub tree is null its automatically a subtree of main tree
        if not subRoot: return True
        
        #If the main tree is null, the subtree cannot be a subtree of it
        #We also know t is not empty from above conditioon so no need to check below
        if not root: return False

        #Checks if subroot is a subtree of root
        if self.sameTree(root, subRoot):
            return True

        #is subtree is recursive, can compare subtree to the subtrees of the root
        
        return  (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
        

        
        
