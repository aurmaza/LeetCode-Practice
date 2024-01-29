class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l,r = 0, len(nums)-1
        p = len(nums)-1
        while l<=r:
            nL = nums[l]**2
            nR = nums[r]**2
            if nL > nR:
                res[p] = nL
                p-=1
                l+=1
            else:
                res[p] = nR
                p-=1
                r-=1
        return res
