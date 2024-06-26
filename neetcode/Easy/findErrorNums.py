class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        rep = 0
        notseen = 0
        seen = set()
        for n in nums:
            if n in seen:
                rep = n
            else:
                seen.add(n)
        
        for n in range(1,len(nums)+1):
            if n not in seen:
                notseen = n
        return [rep,notseen]
            
        
