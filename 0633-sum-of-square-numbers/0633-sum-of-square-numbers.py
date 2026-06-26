class Solution:
    def judgeSquareSum(self,c:int)->bool:
        l=0
        r=int(c**0.5)
        while l<=r:
            s=l*l+r*r
            if s==c:
                return True
            elif s<c:
                l+=1
            else:
                r-=1
        return False