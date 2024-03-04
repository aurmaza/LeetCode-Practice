# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        q.append(root)
        res=[]
        while q:
            qlen=len(q)
            list1=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    list1.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if list1:
                res.append(sum(list1)/len(list1))
        return res
