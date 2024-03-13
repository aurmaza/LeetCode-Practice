class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currentSum = 0
        prefixSums = {0:1}
        for n in nums:
            currentSum += n
            difference = currentSum - k
            res += prefixSums.get(difference,0)
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum,0)
        return res
