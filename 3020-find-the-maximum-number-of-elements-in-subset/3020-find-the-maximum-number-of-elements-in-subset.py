class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt={}
        for x in nums:
            if x in cnt:
                cnt[x]+=1
            else:
                cnt[x]=1
        ans=1
        if 1 in cnt:
            if cnt[1]%2:
                ans=cnt[1]
            else:
                ans=cnt[1]-1
        for x in cnt:
            if x==1:
                continue
            cur=x
            length=0
            while cur in cnt and cnt[cur]>=2:
                length+=2
                cur*=cur
            if cur in cnt and cnt[cur]>=1:
                length+=1
            else:
                length-=1
            if length<1:
                length=1
            if length>ans:
                ans=length
        return ans