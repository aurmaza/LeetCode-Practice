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
    
    # neet solution
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Uses only one set of double loops
        # Boxes consists of a dictionary of sets that have keys (i//3, j//3) which represents the 9 squares 
        # that must all have unique values
        # so a set is created for those 9 squares and their indexes are found by (i//3, j//3)
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if(board[i][j] in rows[i] or
                   board[i][j] in cols[j] or
                   board[i][j] in boxes[(i//3, j//3)] ): return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3, j//3)].add(board[i][j])
        return True  



def isValidSudoku(self,board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    boxes = collections.defaultdict(set) #in location (i//3, j//3) 3x3 board
    for i in range(9):
        for j in range(9)
            #Skip empty box
            if board[i][j] == '.':
                continue
            if(board[i][j] in rows[i] or
               board[i][j] in cols[j] or
               board[i][j] in boxes[(i//3, j//3)]): return False
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            boxes[(i//3,j//3)].add(board[i][j])
    return True

