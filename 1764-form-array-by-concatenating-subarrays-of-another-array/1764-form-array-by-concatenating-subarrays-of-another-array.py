class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i=0
        j=0
        while i<len(groups) and j<len(nums):
            if j+len(groups[i])<=len(nums) and nums[j:j+len(groups[i])]==groups[i]:
                j+=len(groups[i])
                i+=1
            else:
                j+=1

        return i==len(groups)