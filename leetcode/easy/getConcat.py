class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newPt = (len(nums)-1)*2 
        nArray = []
        for n in nums:
            nArray.append(n)
        for n in nums:
            nArray.append(n)
        return nArray
