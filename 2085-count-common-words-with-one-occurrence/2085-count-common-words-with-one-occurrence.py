class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a={}
        b={}
        for x in words1:
            a[x]=a.get(x,0)+1
        for x in words2:
            b[x]=b.get(x,0)+1
        res=0
        for x in a:
            if a[x]==1 and b.get(x,0)==1:
                res+=1
        return res