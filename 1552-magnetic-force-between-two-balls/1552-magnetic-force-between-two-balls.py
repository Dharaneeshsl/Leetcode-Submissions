class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ball=0
        position.sort()
        def check(mid):
            ball=1
            last=position[0]

            for i in range(1,len(position)):
                if position[i]-last>=mid:
                    ball+=1
                    last=position[i]
                    if ball>=m:
                        return True
            return False

        l=1
        r=position[-1]-position[0]
        ans=-1

        while(l<=r):
            mid=(l+r)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
