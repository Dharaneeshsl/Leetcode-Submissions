class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans=[]
        def dfs(i,path,val,prev):
            if i==len(num):
                if val==target:
                    ans.append(path)
                return
            for j in range(i,len(num)):
                if j>i and num[i]=='0':
                    break
                cur=num[i:j+1]
                n=int(cur)
                if i==0:
                    dfs(j+1,cur,n,n)
                else:
                    dfs(j+1,path+'+'+cur,val+n,n)
                    dfs(j+1,path+'-'+cur,val-n,-n)
                    dfs(j+1,path+'*'+cur,val-prev+prev*n,prev*n)
        dfs(0,"",0,0)
        return ans