class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp={0:0}
        for r in rods:
            cur=dp.copy()

            for diff,height in dp.items():
                cur[diff+r]=max(cur.get(diff+r,0),height)
                cur[diff-r]=max(cur.get(diff-r,0),height+r)
            dp=cur
        return dp.get(0,0)