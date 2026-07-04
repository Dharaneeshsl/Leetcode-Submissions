class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        currmin=nums[0]
        currmax=nums[0]
        maxSum=nums[0]
        minSum=nums[0]
        for i in range(1,len(nums)):
            currmax=max(nums[i],currmax+nums[i])
            maxSum=max(maxSum,currmax)

            currmin=min(nums[i],currmin+nums[i])
            minSum=min(minSum,currmin)

        if maxSum<0:
            return maxSum
            
        return max(total-minSum,maxSum)