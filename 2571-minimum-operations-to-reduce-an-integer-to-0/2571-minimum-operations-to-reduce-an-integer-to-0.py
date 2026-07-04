class Solution:
    def minOperations(self, n: int) -> int:
        ops=0
        while n>0:
            if n==1:
                ops+=1
                break
            if n%2==0:
                n//=2
            else:
                if n%4==1:
                    n-=1
                if n%4==3:
                    n+=1
                ops+=1
        
        return ops
