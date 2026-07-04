class Solution:
    def shortestPalindrome(self,s:str)->str:
        if not s:
            return s
        base=131
        mod=10**9+7
        n=len(s)
        r=s[::-1]
        pre=0
        rev=0
        power=1
        best=0
        for i in range(n):
            pre=(pre*base+ord(s[i]))%mod
            rev=(rev+ord(s[i])*power)%mod
            if pre==rev:
                best=i+1
            power=(power*base)%mod
        return r[:n-best]+s