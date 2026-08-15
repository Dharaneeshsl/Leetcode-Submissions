class Solution:
    def generateMatrix(self,n):
        a=[[0]*n for _ in range(n)]
        top,bottom,left,right=0,n-1,0,n-1
        x=1
        while top<=bottom and left<=right:
            for j in range(left,right+1):
                a[top][j]=x
                x+=1
            top+=1
            for i in range(top,bottom+1):
                a[i][right]=x
                x+=1
            right-=1
            if top<=bottom:
                for j in range(right,left-1,-1):
                    a[bottom][j]=x
                    x+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    a[i][left]=x
                    x+=1
                left+=1
        return a