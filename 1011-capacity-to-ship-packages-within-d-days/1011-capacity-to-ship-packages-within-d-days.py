class Solution:
    def shipWithinDays(self,weights:List[int],days:int)->int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=(l+r)//2
            d=1
            s=0
            for w in weights:
                if s+w>m:
                    d+=1
                    s=0
                s+=w
            if d<=days:
                r=m
            else:
                l=m+1
        return l