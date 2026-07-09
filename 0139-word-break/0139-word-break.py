class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)+1
        dp=[False]*(n)
        dp[0]=True

        for i in range(len(dp)):
            for x in wordDict:
                if i-len(x)>=0 and s[i-len(x):i]==x and dp[i-len(x)]:
                    dp[i]=True
                    break


        return dp[n-1]