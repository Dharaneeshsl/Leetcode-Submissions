class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target=len(nums)//3+1
        hs={}
        for x in nums:
            hs[x]=hs.get(x,0)+1
        res=[]
        for x,y in hs.items():
            if y>=target:
                res.append(x)
            
        return res
        