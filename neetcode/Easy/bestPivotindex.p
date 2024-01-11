class Solution:
    
    def createSumArrays(self, nums: List[int]):
        sumArrayLeft = []
        sumArrayRight = []
        for m in range(len(nums)):
            sumArrayLeft.append(sum(nums[:m]))
        for n in range(len(nums)):
            sumArrayRight.append(sum(nums[n+1:len(nums)]))
            
        return sumArrayLeft, sumArrayRight
    def pivotIndex(self, nums: List[int]) -> int:
        arrayLeft, arrayRight = self.createSumArrays(nums)
        print(arrayLeft, arrayRight)
        for n in range(len(nums)):
            if arrayLeft[n] == arrayRight[n]:
                return n
        return -1
        
