from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for _ in range(n)]

        def convertFormat():
            return  [''.join(row) for row in board]

        def isValid(row,col):
            for i in range(n):
                if board[row][i]=='Q':
                    return False
                if board[i][col]=='Q':
                    return False
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            return True
        
        def NQueens(row):
            if row==n:
                res.append(convertFormat())
                return
            for col in range(n):
                if isValid(row,col):
                    board[row][col]='Q'
                    NQueens(row+1)
                    board[row][col]='.'
        NQueens(0)
        return res
