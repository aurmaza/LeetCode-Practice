class Solution:
    def pivotInteger(self, n: int) -> int:
        a = []
        for i in range(1,n+1):
            a.append(i)
        print(a)
        for i in range(n):
            left = a[:i+1]
            right = a[i:n+1]
            if sum(left) == sum(right):
                return i+1
        return -1
