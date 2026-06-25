class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        lmax=float("-inf")
        rmax=float("-inf")
        total=0
        while left<right:
            if height[left]<height[right]:
                lmax=max(height[left],lmax)
                if lmax-height[left]>0:
                    total+=lmax-height[left]
                left+=1
            else:
                rmax=max(height[right],rmax)
                if rmax-height[right]>0:
                    total+=rmax-height[right]
                right-=1
        return total

        