class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = set()
        for i in nums:
            t.add(i)
        
        return len(nums) != len(t)