class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == val:
                i+=1
                continue
            else:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j
        
