# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        averages = []

        while queue:
            lvlLen = len(queue)
            lvlSum = 0
            for n in range(lvlLen):
                node = queue.pop(0)
                lvlSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(lvlSum/lvlLen)
        return averages
