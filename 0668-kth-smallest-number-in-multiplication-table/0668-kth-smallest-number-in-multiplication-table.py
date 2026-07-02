class Solution:
    def findKthNumber(self,m:int,n:int,k:int)->int:
        l,r=1,m*n
        while l<r:
            mid=(l+r)//2
            c=0
            for i in range(1,m+1):
                c+=min(n,mid//i)
            if c>=k:
                r=mid
            else:
                l=mid+1
        return l