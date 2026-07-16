class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans=0
        for i in range(32):
            abit=(a>>i)&1
            bbit=(b>>i)&1
            cbit=(c>>i)&1

            if cbit==1:
                if abit==0 and bbit==0:
                    ans+=1
            else:
                ans+=abit+bbit
        return ans