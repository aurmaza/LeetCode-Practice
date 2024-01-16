class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans  = []
        n1 = set()
        n2 = set()
        for n in range(len(nums1)):
            if nums1[n] not in nums2:
                n1.add(nums1[n])
        for m in range(len(nums2)):
            if nums2[m] not in nums1:
                n2.add(nums2[m])
        return [n1,n2]

        
