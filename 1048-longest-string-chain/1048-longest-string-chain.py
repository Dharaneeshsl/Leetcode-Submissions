class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp={}
        ans=1
        for w in words:
            dp[w]=1
            for i in range(len(w)):
                p=w[:i]+w[i+1:]
                dp[w]=max(dp[w],dp.get(p,0)+1)
            ans=max(ans,dp[w])
        return ans