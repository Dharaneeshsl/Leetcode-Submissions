class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 + j//3].add(num)

        def isValid(num, row, col):
            return (num not in rows[row] and
                    num not in cols[col] and
                    num not in boxes[(row//3)*3 + col//3])
        
        def filltheboard():
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for num in '123456789':
                            if isValid(num,i,j):
                                board[i][j]=num
                                rows[i].add(num)
                                cols[j].add(num)
                                boxes[(i//3)*3+j//3].add(num)
                                if filltheboard(): return True
                                board[i][j]='.'
                                rows[i].remove(num)
                                cols[j].remove(num)
                                boxes[(i//3)*3+j//3].remove(num)
                        return False
            return True
        filltheboard()