class Solution:
    def splitArray(self,nums:List[int],k:int)->int:
        def canSplit(limit):
            groups=1
            curr=0
            for x in nums:
                if curr+x<=limit:
                    curr+=x
                else:
                    groups+=1
                    curr=x
            return groups<=k
        left=max(nums)
        right=sum(nums)
        ans=right
        while left<=right:
            mid=(left+right)//2
            if canSplit(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans