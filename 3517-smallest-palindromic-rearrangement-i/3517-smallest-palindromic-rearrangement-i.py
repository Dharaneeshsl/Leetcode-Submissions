class Solution:
    def smallestPalindrome(self, s: str) -> str:
        res=sorted(s)
        hs={}
        for x in res:
            hs[x]=hs.get(x,0)+1
        left=[]
        middle=''
        for x in sorted(hs):
            left.append(x*(hs[x]//2))
            if hs[x]%2:
                middle=x
        left=''.join(left)
        return left+middle+left[::-1]
