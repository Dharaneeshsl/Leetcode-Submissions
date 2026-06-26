class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans=[]
        for q in queries:
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<=q:
                    l=mid+1
                else:
                    r=mid-1
            ans.append(l)
        return ans