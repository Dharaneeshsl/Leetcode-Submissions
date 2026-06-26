import heapq
class Solution:
    def lastStoneWeight(self, stones):
        maxHeap = [-s for s in stones]  
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)  
            x = -heapq.heappop(maxHeap) 

            if x != y:
                heapq.heappush(maxHeap, -(y - x))

        return -maxHeap[0] if maxHeap else 0