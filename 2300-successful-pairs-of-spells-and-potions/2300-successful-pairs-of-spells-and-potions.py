class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        n=len(potions)
        for spell in spells:
            left=0
            right=n-1
            idx=n
            while left<=right:
                mid=(left+right)//2
                if spell*potions[mid]>=success:
                    idx=mid
                    right=mid-1
                else:
                    left=mid+1

            ans.append(n-idx)

        return ans