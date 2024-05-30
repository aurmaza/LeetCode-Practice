class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        res = 0
        while l <=r:
            if l == r:
               res += nums[l]
            else:
                res += int(str(nums[l]) + str(nums[r])) 
            l+=1
            r-=1
        return res
