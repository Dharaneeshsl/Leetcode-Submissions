class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def valid(divisor):
            total=0
            for num in nums:
                total+=(num+divisor-1)//divisor
            return total<=threshold
        l,r=1,max(nums)
        while l<r:
            mid=(l+r)//2
            if valid(mid):
                r=mid
            else:
                l=mid+1
        return l
        