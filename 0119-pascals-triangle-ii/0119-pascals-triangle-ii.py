class Solution:
    def getRow(self,rowIndex):
        res=[1]
        for i in range(1,rowIndex+1):
            res.append(res[-1]*(rowIndex-i+1)//i)
        return res