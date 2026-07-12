import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small=[]
        large=[]
        remove=defaultdict(int)
        smallSize=0
        largeSize=0

        def clean(heap,isSmall):
            while heap:
                x=-heap[0] if isSmall else heap[0]
                if remove[x]:
                    remove[x]-=1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal smallSize,largeSize
            if smallSize>largeSize+1:
                heapq.heappush(large,-heapq.heappop(small))
                smallSize-=1
                largeSize+=1
                clean(small,True)
            elif largeSize>smallSize:
                heapq.heappush(small,-heapq.heappop(large))
                largeSize-=1
                smallSize+=1
                clean(large,False)

        def add(x):
            nonlocal smallSize,largeSize
            if not small or x<=-small[0]:
                heapq.heappush(small,-x)
                smallSize+=1
            else:
                heapq.heappush(large,x)
                largeSize+=1
            balance()

        def erase(x):
            nonlocal smallSize,largeSize
            remove[x]+=1
            if x<=-small[0]:
                smallSize-=1
                if x==-small[0]:
                    clean(small,True)
            else:
                largeSize-=1
                if large and x==large[0]:
                    clean(large,False)
            balance()

        def median():
            clean(small,True)
            clean(large,False)
            if k%2:
                return float(-small[0])
            return (-small[0]+large[0])/2

        ans=[]
        for i in range(k):
            add(nums[i])
        ans.append(median())
        for i in range(k,len(nums)):
            add(nums[i])
            erase(nums[i-k])
            ans.append(median())
        return ans