class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #First, find nums[]
        res = []
        for n in nums1:
            index = -1
            if n in nums2:
                index = nums2.index(n)
                numAppend = -1
                for j in range(index,len(nums2)):
                    if nums2[j] > n:
                        numAppend = nums2[j]
                        break

                res.append(numAppend)
            else:
                res.append(-1)
        return res
