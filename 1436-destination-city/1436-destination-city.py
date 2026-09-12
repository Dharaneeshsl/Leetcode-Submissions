class Solution:
    def destCity(self,paths:List[List[str]])->str:
        hs={a for a,b in paths}
        for a,b in paths:
            if b not in hs:return b