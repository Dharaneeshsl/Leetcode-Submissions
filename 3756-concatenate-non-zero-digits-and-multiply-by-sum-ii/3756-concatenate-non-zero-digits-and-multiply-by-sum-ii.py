class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod=1000000007
        pos=[]
        pre=[0]
        for i in range(len(s)):
            if s[i]!='0':
                pos.append(i)
                pre.append((pre[-1]*10+ord(s[i])-48)%mod)
        m=len(pos)
        pw=[1]*(m+1)
        for i in range(1,m+1):
            pw[i]=pw[i-1]*10%mod
        ps=[0]
        for i in range(m):
            ps.append(ps[-1]+ord(s[pos[i]])-48)
        ans=[]
        for l,r in queries:
            lo=0
            hi=m
            while lo<hi:
                mid=(lo+hi)//2
                if pos[mid]<l:
                    lo=mid+1
                else:
                    hi=mid
            a=lo
            lo=0
            hi=m
            while lo<hi:
                mid=(lo+hi)//2
                if pos[mid]<=r:
                    lo=mid+1
                else:
                    hi=mid
            b=lo
            if a==b:
                ans.append(0)
                continue
            ln=b-a
            x=(pre[b]-pre[a]*pw[ln])%mod
            sm=ps[b]-ps[a]
            ans.append(x*sm%mod)
        return ans