class Solution:
    def longestIncreasingPath(self,matrix:List[List[int]])->int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]
            dp[i][j]=1
            for x,y in d:
                ni=i+x
                nj=j+y
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>matrix[i][j]:
                    dp[i][j]=max(dp[i][j],1+dfs(ni,nj))
            return dp[i][j]
        ans=0
        for i in range(m):
            for j in range(n):
                ans=max(ans,dfs(i,j))
        return ans