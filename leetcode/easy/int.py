class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nSet1 = set(nums1)
        nSet2 = set(nums2)
        res = []
        for n in nSet1:
            if n in nSet2:
                res.append(n)
        return res
