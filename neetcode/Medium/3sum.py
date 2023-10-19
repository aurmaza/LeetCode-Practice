class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                numSum = a + nums[l] + nums[r]
                if numSum > 0:
                    r-=1
                elif numSum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    r-=1
                    while nums[r+1] == nums[r] and l<r:
                        r-=1
        return res