class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        a=0
        x=max(1,n-k)
        for i in range(x,n+k+1):
            if (n&i)==0:
                a+=i
        return a