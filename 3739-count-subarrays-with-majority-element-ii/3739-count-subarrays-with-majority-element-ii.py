class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        p=[0]
        s=0
        for x in nums:
            if x==target:
                s+=1
            else:
                s-=1
            p.append(s)
        v=sorted(set(p))
        d={}
        for i,x in enumerate(v):
            d[x]=i+1
        b=[0]*(len(v)+2)
        def add(i):
            while i<len(b):
                b[i]+=1
                i+=i&-i
        def get(i):
            r=0
            while i:
                r+=b[i]
                i-=i&-i
            return r
        ans=0
        for x in p:
            ans+=get(d[x]-1)
            add(d[x])
        return ans