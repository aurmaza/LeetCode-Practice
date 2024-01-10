class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n ,0) + 1

        return max(dic, key=dic.get)
