class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        res=[]
        for i in range(len(equations)):
            a=equations[i][0]
            b=equations[i][1]
            val=values[i]
            graph[a].append((b,val))
            graph[b].append((a,1/val))


        def dfs(node,target,visited,product):
            if node==target:
                return product
            visited.add(node)
            for y,val in graph[node]:
                if y not in visited:
                    ans=dfs(y,target,visited,product*val)
                    if ans!=-1:
                        return ans
            return -1

        for i in range(len(queries)):
            x=queries[i][0]
            y=queries[i][1]
            if x not in graph or y not in graph:
                res.append(-1.00000)
            
            elif x==y:
                res.append(1.00000)

            else:
                res.append(dfs(x,y,set(),1))
        
        return res