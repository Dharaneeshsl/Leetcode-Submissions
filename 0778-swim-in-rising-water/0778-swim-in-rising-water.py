class Solution:
    def swimInWater(self, grid):
        n=len(grid)
        def dfs(r, c, time, visit):
            if (r<0 or c<0 or r>=n or c>=n or (r, c) in visit or grid[r][c] > time):
                return False

            if r==n-1 and c==n-1:
                return True

            visit.add((r, c))
            return (
                dfs(r + 1, c, time, visit) or
                dfs(r - 1, c, time, visit) or
                dfs(r, c + 1, time, visit) or
                dfs(r, c - 1, time, visit)
            )

        left=grid[0][0]
        right=n*n

        while left<right:

            mid=(left+right)//2
            visit=set()
            if dfs(0, 0,mid,visit):
                right=mid
            else:
                left=mid+1

        return left