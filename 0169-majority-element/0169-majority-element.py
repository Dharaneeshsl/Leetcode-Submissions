class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=0
        sum=0
        for x in nums:
            if sum==0:
                candidate=x
                sum=1
            elif x==candidate:
                sum+=1
            else:
                sum-=1
        return candidate