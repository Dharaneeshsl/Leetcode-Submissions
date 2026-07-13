import heapq
from collections import defaultdict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap=[]
        min_heap=[]
        heap_dict=defaultdict(int)
        ans=[]
        for i in range(k):
            heapq.heappush(max_heap,-nums[i])
        for _ in range(k//2):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        if k%2:
            median=float(-max_heap[0])
        else:
            median=(-max_heap[0]+min_heap[0])/2
        ans.append(median)
        for i in range(k,len(nums)):
            prev_num=nums[i-k]
            heap_dict[prev_num]+=1
            balance=-1 if prev_num<=median else 1
            if nums[i]<=median:
                balance+=1
                heapq.heappush(max_heap,-nums[i])
            else:
                balance-=1
                heapq.heappush(min_heap,nums[i])
            if balance<0:
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            elif balance>0:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
            while max_heap and heap_dict[-max_heap[0]]>0:
                heap_dict[-max_heap[0]]-=1
                heapq.heappop(max_heap)
            while min_heap and heap_dict[min_heap[0]]>0:
                heap_dict[min_heap[0]]-=1
                heapq.heappop(min_heap)
            if k%2:
                median=float(-max_heap[0])
            else:
                median=(-max_heap[0]+min_heap[0])/2
            ans.append(median)

        return ans