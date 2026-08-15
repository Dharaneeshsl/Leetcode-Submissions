class Solution:
    def diffWaysToCompute(self,expression):
        res=[]
        for i,c in enumerate(expression):
            if c in "+-*":
                left=self.diffWaysToCompute(expression[:i])
                right=self.diffWaysToCompute(expression[i+1:])
                for a in left:
                    for b in right:
                        if c=="+":
                            res.append(a+b)
                        elif c=="-":
                            res.append(a-b)
                        else:
                            res.append(a*b)
        if not res:
            res.append(int(expression))
        return res