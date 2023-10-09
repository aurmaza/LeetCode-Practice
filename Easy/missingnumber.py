class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        
        for num in range(0,len(nums)):
            res ^= num
            res ^= nums[num]
        return res


        