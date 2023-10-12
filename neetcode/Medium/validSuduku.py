class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Checks for dupes in rows
        for i in range(0,9):
            rowcheck = set()
            for j in range(0,9):
                
                if board[i][j] not in rowcheck:
                    if board[i][j] != '.':
                        rowcheck.add(board[i][j])
                else:
                    
                    return False

        #Checks for Dupes in columns
        for i in range(0,9):
            colcheck = set()
            for j in range(0,9):
                print(j,i)
                if board[j][i] not in colcheck:
                    if board[j][i] != '.':
                        colcheck.add(board[j][i])
        
                else:
                    return False
        # Checks for dupes in existing boxes        
        for i in range(0,9, 3):
            for j in range(0,9, 3):
                boxCheck = set()
                for k in range(3):
                    for l in range(3):
                        val = board[i+k][j+l]
                        if val == '.':
                            continue
                        if val in boxCheck:
                            return False
                        boxCheck.add(val)
                    
        return True
        

        