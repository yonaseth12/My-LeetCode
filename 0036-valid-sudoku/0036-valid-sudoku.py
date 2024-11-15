class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Check 1
        for i in board:
            unique = set()
            for j in i:
                if j == '.': continue
                if j in unique: return False
                else: unique.add(j)
        #Check 2
        for i in range(9):
            unique = set()
            for j in range(9):
                if board[j][i] == '.': continue
                if board[j][i] in unique: return False
                else: unique.add(board[j][i])
        #Check 3
        for i in range(0, 7, 3):          #Row_block
            for j in range(0, 7, 3):      #Column_block
                unique = set()
                for k in range(3):        #Iterator_row
                    for l in range(3):    #Iterator_column
                        if board[i+k][j+l] == '.': continue
                        if board[i+k][j+l] in unique: return False
                        else: unique.add(board[i+k][j+l])           
        return True