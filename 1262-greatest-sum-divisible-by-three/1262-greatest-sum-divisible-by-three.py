class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0,float("-inf"),float("-inf")]
        for x in nums:
            ndp=dp[:]
            for r in range(3):
                ndp[(r+x)%3]=max(ndp[(r+x)%3],dp[r]+x)
            dp=ndp
        return dp[0]