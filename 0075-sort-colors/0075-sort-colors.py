class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0
        y=0
        z=0
        for i in nums:
            if i==0:
                x+=1
            elif i==2:
                z+=1
            else:
                y+=1
            
        for i in range(len(nums)):
            if x>0:
                nums[i]=0
                x-=1
            elif y>0:
                nums[i]=1
                y-=1
            else:
                nums[i]=2
                z-=1
        