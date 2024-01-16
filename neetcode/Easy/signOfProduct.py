class Solution:
    def signFunc(self, num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product *= n
        return self.signFunc(product)
