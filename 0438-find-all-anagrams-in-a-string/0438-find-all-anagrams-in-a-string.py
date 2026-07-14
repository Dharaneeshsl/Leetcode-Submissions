class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        hs1={}
        hs2={}
        if len(s)<len(p):
            return []
        for x in p:
            hs1[x]=hs1.get(x,0)+1
        
        for i in range(len(p)):
            hs2[s[i]]=hs2.get(s[i],0)+1
        
        if hs1==hs2:
            res.append(0)
        
        for i in range(len(p),len(s)):
            hs2[s[i-len(p)]]-=1
            if hs2[s[i-len(p)]]==0:
                del hs2[s[i-len(p)]]
            hs2[s[i]]=hs2.get(s[i],0)+1
            if hs1==hs2:
                res.append(i-len(p)+1)
            
        return res
        
         

        