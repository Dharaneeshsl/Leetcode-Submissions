class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi=0
        nums=list(set(nums))
        nums.sort()
        count=1
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
            else:
                count=1
            maxi=max(maxi,count)
                
        return maxi