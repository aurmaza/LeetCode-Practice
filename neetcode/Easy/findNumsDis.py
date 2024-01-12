class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for n in range(len(nums)):
            numAt = abs(nums[n]) - 1
            nums[numAt] = -1 * abs(nums[numAt])
            
        for n in range(len(nums)):
            if nums[n] > 0:
                res.append(n+1)
        return res
