class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = {}
        numList[target-nums[0]] = 0
        for i in range(1, len(nums)):
            needed = target - nums[i]
            if nums[i] in numList:
                
                return [numList[nums[i]] ,i]
            
            numList[needed] = i
#Cleaner way
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        dic[nums[0]] = 0
        for i in range(1, len(nums)):
            numNeeded = target - nums[i]
            if numNeeded in dic.keys():
                return [dic[numNeeded],i]
            else:
                dic[nums[i]] = i