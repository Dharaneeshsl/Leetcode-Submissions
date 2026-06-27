import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q=sorted((x,i) for i,x in enumerate(queries))
        res=[-1]*len(queries)
        heap=[]
        i=0

        for val,idx in q:
            while i<len(intervals) and intervals[i][0]<=val:
                l,r=intervals[i]
                heapq.heappush(heap,(r-l+1,r))
                i+=1

            while heap and heap[0][1]<val:
                heapq.heappop(heap)

            if heap:
                res[idx]=heap[0][0]

        return res