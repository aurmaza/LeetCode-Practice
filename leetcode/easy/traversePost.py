"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, root, out):
        if not root: return

        for child in root.children:
            self.traverse(child, out)
        out.append(root.val)
    def postorder(self, root: 'Node') -> List[int]:
        out = []
        self.traverse(root,out)
        return out
