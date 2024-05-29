class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        left, right, out = [None]*n,[None]*n,[None]*n
        temp = float("inf")
        for i in range(n):
            if s[i] == c:
                temp = 0
            left[i] = temp
            temp+=1
        temp = float("inf")
        for i in range(n-1, -1, -1):
            if s[i] == c:
                temp = 0
            right[i] = temp
            temp+=1
        for i in range(n):
            out[i] = min(left[i],right[i])
        return out