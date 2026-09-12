class Solution:
    def findJudge(self,n:int,trust:List[List[int]])->int:
        hs=[0]*(n+1)
        for a,b in trust:
            hs[a]-=1
            hs[b]+=1
        for i in range(1,n+1):
            if hs[i]==n-1:
                return i
        return -1