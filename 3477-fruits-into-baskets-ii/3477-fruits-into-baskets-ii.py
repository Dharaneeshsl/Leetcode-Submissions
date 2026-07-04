class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        used=[False]*n
        ans=0

        for f in fruits:
            ok=False
            for i in range(n):
                if not used[i] and baskets[i]>=f:
                    used[i]=True
                    ok=True
                    break
            if not ok:
                ans+=1

        return ans