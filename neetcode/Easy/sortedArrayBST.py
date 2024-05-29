# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def helper(l,r): 
        if l > r:
            return None
        mid = (l+r)//2
        root = TreeNode(val=nums[mid])
        root.left = helper(l, mid-1)
        root.right = helper(mid+1,r)
        return root
    res = helper(0,len(nums)-1)
    return res 
    

nums = [-10,-3,0,5,9]
res = sortedArrayToBST(nums)
print(res)    


