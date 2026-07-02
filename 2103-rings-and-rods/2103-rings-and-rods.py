class Solution:
    def countPoints(self,rings:str)->int:
        a=[0]*10
        m={"R":1,"G":2,"B":4}
        for i in range(0,len(rings),2):
            c=int(rings[i+1])
            a[c]|=m[rings[i]]
        return sum(x==7 for x in a)