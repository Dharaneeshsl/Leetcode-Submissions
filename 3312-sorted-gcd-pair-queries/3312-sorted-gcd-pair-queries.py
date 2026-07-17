class Solution:
    def gcdValues(self,nums:List[int],queries:List[int])->List[int]:
        m=max(nums)
        f=[0]*(m+1)
        for x in nums:
            f[x]+=1
        c=[0]*(m+1)
        for i in range(1,m+1):
            for j in range(i,m+1,i):
                c[i]+=f[j]
        e=[0]*(m+1)
        for i in range(m,0,-1):
            if c[i]>=2:
                e[i]=c[i]*(c[i]-1)//2
            for j in range(i*2,m+1,i):
                e[i]-=e[j]
        p=[0]*(m+1)
        for i in range(1,m+1):
            p[i]=p[i-1]+e[i]
        return[bisect_right(p,q) for q in queries]