class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum
        
            
        for i in range(k,len(nums)):
            print(i)
            currentSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, currentSum)
        return maxSum/k
