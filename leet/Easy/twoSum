class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = {}
        numList[target-nums[0]] = 0
        for i in range(1, len(nums)):
            needed = target - nums[i]
            if nums[i] in numList:
                
                return [numList[nums[i]] ,i]
            
            numList[needed] = i
            
