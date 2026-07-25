class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left=[]
        right=[]
        i=0
        j=len(costs)-1
        ans=0
        while i<=j and len(left)<candidates:
            heappush(left,costs[i])
            i+=1
        while i<=j and len(right)<candidates:
            heappush(right,costs[j])
            j-=1
        for _ in range(k):
            if not right or (left and left[0]<=right[0]):
                ans+=heappop(left)
                if i<=j:
                    heappush(left,costs[i])
                    i+=1
            else:
                ans+=heappop(right)
                if i<=j:
                    heappush(right,costs[j])
                    j-=1

        return ans