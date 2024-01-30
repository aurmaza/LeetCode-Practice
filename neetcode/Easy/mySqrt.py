class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x

        while l<=r:
            mid = (l+r)//2
            sqrt = mid * mid
            print(l,r,mid,sqrt)
            if sqrt > x:
                r = mid - 1
            elif sqrt < x:
                l = mid + 1
            else:
                return int(mid)
                
        return r
