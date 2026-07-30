class Solution:
    def imageSmoother(self,img:List[List[int]])->List[List[int]]:
        m,n=len(img),len(img[0])
        res=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s=c=0
                for x in range(max(0,i-1),min(m,i+2)):
                    for y in range(max(0,j-1),min(n,j+2)):
                        s+=img[x][y]
                        c+=1
                res[i][j]=s//c
        return res