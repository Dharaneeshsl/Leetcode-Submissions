class Solution:
    def totalNQueens(self,n:int)->int:
        board=[['.']*n for _ in range(n)]
        ans=0
        def valid(r,c):
            for i in range(r):
                if board[i][c]=='Q':
                    return False
            i,j=r-1,c-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i,j=r-1,c+1
            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True
        def solve(row):
            nonlocal ans
            if row==n:
                ans+=1
                return
            for col in range(n):
                if valid(row,col):
                    board[row][col]='Q'
                    solve(row+1)
                    board[row][col]='.'

        solve(0)
        return ans