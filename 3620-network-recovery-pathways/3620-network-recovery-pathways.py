import heapq
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n= len(online)
        l=float("inf")
        r=float("-inf")

        graph=defaultdict(list)

        for u,v,w in edges:
            if v != n - 1 and not online[v]:
                continue
            
            graph[u].append((v,w))
            l=min(l,w)
            r=max(r,w)

        def check(graph,k,mid):
            pq=[(0,0)]

            dist = [float("inf")] * n
            dist[0] = 0
            while pq:
                d,node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                if d>k:
                    continue
                if node==n-1:
                    return True
                
                for neigh,cost in graph[node]:
                    if cost < mid:
                        continue
                    if d + cost < dist[neigh]:
                        dist[neigh] = d + cost
                        heapq.heappush(pq, (d + cost, neigh))

            return False

        ans=-1
        while(l<=r):
            mid=(l+r)//2
            if check(graph,k,mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans