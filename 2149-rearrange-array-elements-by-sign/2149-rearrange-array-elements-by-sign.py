class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res1=[]
        res2=[]
        res=[]
        for x in nums:
            if x>0:
                res1.append(x)
            elif x<0:
                res2.append(x)

        i=0
        k=0
        while k<len(nums):
            res.append(res1[i])
            res.append(res2[i])
            i+=1
            k+=2
        return res


            