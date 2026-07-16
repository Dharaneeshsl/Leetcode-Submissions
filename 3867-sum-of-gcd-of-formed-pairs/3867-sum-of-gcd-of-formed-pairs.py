from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        res=[]
        mx=-1
        for i in range(len(nums)):
            mx=max(mx,nums[i])
            res.append(gcd(nums[i],mx))

        res.sort()
        sum=0
        if len(res)%2==1:
            i=0
            j=len(res)-1
            while i<j:
                sum+=gcd(res[i],res[j])
                i+=1
                j-=1
        else:
            i=0
            j=len(res)-1
            while i<j:
                sum+=gcd(res[i],res[j])
                i+=1
                j-=1
        return sum
