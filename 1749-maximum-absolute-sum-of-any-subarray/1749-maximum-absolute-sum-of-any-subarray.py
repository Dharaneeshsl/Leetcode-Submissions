class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currMax=maxSum=nums[0]
        currMin=minSum=nums[0]
        for i in range(1,len(nums)):
            currMax=max(nums[i],currMax+nums[i])
            maxSum=max(maxSum,currMax)
            currMin=min(nums[i],currMin+nums[i])
            minSum=min(minSum,currMin)
        return max(maxSum,abs(minSum))