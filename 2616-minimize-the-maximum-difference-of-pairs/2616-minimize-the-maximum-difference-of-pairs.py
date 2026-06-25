class Solution:
    def minimizeMax(self,nums:List[int],p:int)->int:
        nums.sort()
        def can(mid):
            cnt=0
            i=1
            while i<len(nums):
                if nums[i]-nums[i-1]<=mid:
                    cnt+=1
                    i+=2
                else:
                    i+=1
            return cnt>=p

        l=0
        r=nums[-1]-nums[0]

        while l<r:
            mid=(l+r)//2
            if can(mid):
                r=mid
            else:
                l=mid+1

        return l