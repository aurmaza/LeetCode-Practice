class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = 0
        dic = {0:-1}
        count = 0
        for i,n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count in dic: m = max(m, i - dic[count])
            else: dic[count] = i
        return m
