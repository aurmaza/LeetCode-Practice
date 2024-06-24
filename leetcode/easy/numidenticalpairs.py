class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        for n in range(0,len(nums)):
            m[nums[n]] = m.get(nums[n], 0) + 1
        count = 0
        for q in m.values():
            count+= (q*(q-1)//2)
        return count
