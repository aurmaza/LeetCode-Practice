class Solution:
    def increasing(self, nums):
        prev = nums[0]
        for n in range(1,len(nums)):
            if nums[n] < prev:
                return False
            prev = nums[n]
        return True
    def decreasing(self, nums):
        prev = nums[0]
        for n in range(1,len(nums)):
            if nums[n] > prev:
                return False
            prev = nums[n]
        return True
    def isMonotonic(self, nums: List[int]) -> bool:
        res = False
        prev = nums[0]
        for n in range(1,len(nums)):
            if nums[n] > prev:
                return self.increasing(nums)
            if nums[n] < prev:
                return self.decreasing(nums)
            else:
                continue
            prev = nums[n]
        return True
