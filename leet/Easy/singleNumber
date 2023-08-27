class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            #XOR Operator
            #Returns 1 if the bits differ
            #Returns 0 if they are same
            #1001
            #^
            #0101
            #1100
            #
            #doing this on the entire array singles out the only duplicate.
            res = num ^ res
        return res
