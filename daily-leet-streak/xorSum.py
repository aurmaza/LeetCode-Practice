#https://leetcode.com/problems/sum-of-all-subset-xor-totals/submissions/1262650707/?envType=daily-question&envId=2024-05-20
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res << (len(nums)-1)
