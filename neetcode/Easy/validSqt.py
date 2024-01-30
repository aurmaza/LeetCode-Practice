class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 2, num // 2
        if num < 4:
            return num == 1
        
        
        while l<=r:
            
            mid = l+((r-l) // 2)
            sqd = mid*mid
            print(l,r,mid,sqd)
            if sqd > num:
                r = mid-1
            elif sqd < num:
                l = mid + 1
            else:
                return True
        return False
