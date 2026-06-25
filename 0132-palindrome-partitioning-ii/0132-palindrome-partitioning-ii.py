class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                j=i+l
                if i==j:
                    dp[i][j]=True
                elif s[i]==s[j] and(j==i+1 or dp[i+1][j-1]):
                    dp[i][j]=True
                else:
                    dp[i][j]=False
        
        cuts=[0]*n
        for i in range(1,n):
            cuts[i]=i
            for j in range(0,i+1):
                if dp[j][i]:
                    if j == 0:
                        cuts[i] = 0
                    else:
                        cuts[i] = min(cuts[i], 1 + cuts[j-1])
        return cuts[n-1]

        
