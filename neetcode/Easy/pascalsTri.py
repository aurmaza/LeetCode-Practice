class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numList = [[1]]
        if numRows > 1:
            for n in range(1,numRows):
                temp = [0] * (n+1)
                temp[0] = 1
                temp[n] = 1
                if n > 1:
                    for j in range(1, n):
                        temp[j] = numList[n-1][j-1] + numList[n-1][j]
                numList.append(temp)
        return numList
