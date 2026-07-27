class Solution:
    def numTilePossibilities(self,tiles:str)->int:
        c={}
        for i in tiles:c[i]=c.get(i,0)+1
        def f():
            s=0
            for i in c:
                if c[i]:
                    s+=1
                    c[i]-=1
                    s+=f()
                    c[i]+=1
            return s
        return f()