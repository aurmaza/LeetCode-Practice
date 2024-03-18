class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = None
        res = []
        for n in range(len(nums)):
            if n < len(nums)-1 and nums[n+1] - nums[n] == 1:
                if start is None:
                    start = nums[n]
            else:
                if start is None:
                    res.append(str(nums[n]))
                else:
                    res.append(f"{start}->{nums[n]}")
                    start = None
        return res
