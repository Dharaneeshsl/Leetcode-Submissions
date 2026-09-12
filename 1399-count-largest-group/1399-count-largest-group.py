class Solution:
    def countLargestGroup(self,n:int)->int:
        hs={}
        for x in range(1,n+1):
            s=sum(map(int,str(x)))
            hs[s]=hs.get(s,0)+1
        maxi=max(hs.values())
        return sum(v==maxi for v in hs.values())