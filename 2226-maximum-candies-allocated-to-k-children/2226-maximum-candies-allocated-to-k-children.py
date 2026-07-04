class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            count=0
            for i in candies:
                count+=i//mid
            
            return count>=k

        ans=0
        l=1
        r=max(candies)
        while(l<=r):
            mid=(l+r)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
