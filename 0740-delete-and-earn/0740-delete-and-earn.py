class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_num=max(nums)
        points=[0]*(max_num + 1)
        for num in nums:
            points[num]+=num
        prev2=0
        prev1=0

        for value in points:
            curr=max(prev1, value + prev2)
            prev2=prev1
            prev1=curr

        return prev1