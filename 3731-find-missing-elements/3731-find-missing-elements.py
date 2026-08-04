class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(1,len(nums)):
            for x in range(nums[i-1]+1,nums[i]):
                res.append(x)
        return res