class Solution(object):
    def maximumTop(self, nums, k):
        n=len(nums)
        if k==0:
            return nums[0]
        if n==1:
            if k%2==1:
                return -1
            return nums[0]
        maxi=-1
        for i in range(min(n,k-1)):
            maxi=max(maxi,nums[i])
        if k<n:
            maxi=max(maxi,nums[k])
        return maxi

        