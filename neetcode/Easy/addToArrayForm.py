class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = 0
        while k or num or carry:
            i = 0
            j = 0
            
            if k:
                i = k % 10
                k = k // 10
            if num:
                j = num.pop()
            r = i + j + carry
            if r >= 10:
                carry = 1
            else:
                carry = 0
            res.append(r%10)            
        return res[::-1]
