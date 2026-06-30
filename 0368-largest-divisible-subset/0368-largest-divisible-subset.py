class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        dp=[1]*n
        par=[-1]*n
        maxi=0
        idx=0
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    par[i]=j
            if dp[i]>maxi:
                maxi=dp[i]
                idx=i
        ans=[]
        while idx!=-1:
            ans.append(nums[idx])
            idx=par[idx]
        return ans[::-1]