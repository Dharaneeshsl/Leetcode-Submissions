class Solution:
    def longestPalindrome(self, s: str) -> int:
        hs={}
        for x in s:
            hs[x]=hs.get(x,0)+1
        ans=0
        count=0
        for x,y in hs.items():
            if y%2==0:
                ans+=y
            elif y==1:
                count=1
            else:
                ans+=y-1
                count=1
            
        if count:
            ans+=1
        return ans
        