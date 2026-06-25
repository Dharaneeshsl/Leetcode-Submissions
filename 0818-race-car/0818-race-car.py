from collections import deque
class Solution:
    def racecar(self,target:int)->int:
        q=deque([(0,1,0)])
        vis={(0,1)}
        while q:
            pos,speed,step=q.popleft()
            if pos==target:
                return step
            np=pos+speed
            ns=speed*2
            if 0<=np<=2*target and (np,ns) not in vis:
                vis.add((np,ns))
                q.append((np,ns,step+1))
            rs=-1 if speed>0 else 1
            if (pos,rs) not in vis:
                vis.add((pos,rs))
                q.append((pos,rs,step+1))