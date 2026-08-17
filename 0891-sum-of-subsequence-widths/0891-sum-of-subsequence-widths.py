class Solution:
    def sumSubseqWidths(self, nums):
        MOD=10**9+7
        nums.sort()
        n=len(nums)
        ans=0
        power=1
        for i in range(n):
            ans=(ans+nums[i]*(power-pow(2,n-i-1,MOD)))%MOD
            power=power*2%MOD
        return ans