class Solution:
    def numSubarraysWithSum(self,nums:List[int],goal:int)->int:
        d={0:1}
        s=0
        ans=0
        for i in nums:
            s+=i
            ans+=d.get(s-goal,0)
            d[s]=d.get(s,0)+1
        return ans