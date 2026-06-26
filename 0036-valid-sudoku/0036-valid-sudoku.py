class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValid(r, c):
            ch = board[r][c]

            for j in range(9):
                if j != c and board[r][j] == ch:
                    return False

            for i in range(9):
                if i != r and board[i][c] == ch:
                    return False

            sr = (r // 3) * 3
            sc = (c // 3) * 3

            for i in range(sr, sr + 3):
                for j in range(sc, sc + 3):
                    if (i != r or j != c) and board[i][j] == ch:
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and not isValid(i, j):
                    return False

        return True