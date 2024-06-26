"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, root, out):
        if root is None: return
        out.append(root.val)
        for child in root.children:
            self.traverse(child, out)
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        self.traverse(root,out)
        return out
        
        
