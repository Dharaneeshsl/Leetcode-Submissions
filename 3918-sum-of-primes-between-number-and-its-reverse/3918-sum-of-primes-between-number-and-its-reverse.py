class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev=int(str(n)[::-1])
        mn=min(n, rev)
        mx=max(n, rev)

        if mx<2:
            return 0

        prime=[True]*(mx+1)
        prime[0]=prime[1]=False

        for i in range(2,int(mx**0.5)+1):
            if prime[i]:
                for j in range(i*i,mx+1,i):
                    prime[j]=False

        ans=0
        for i in range(max(2,mn),mx+1):
            if prime[i]:
                ans+=i

        return ans