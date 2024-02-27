class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l,r = 0, len(mat)-1
        count = 0
        for i in range(len(mat)):
            if l == r:
                count += mat[i][l]
            else:
                count += mat[i][l]
                count += mat[i][r]
            l+=1
            r-=1
        return count


    
