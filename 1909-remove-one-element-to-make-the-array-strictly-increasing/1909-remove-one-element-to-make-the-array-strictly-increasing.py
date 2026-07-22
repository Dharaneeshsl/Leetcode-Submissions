class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def isincreasing(arr):
            for i in range(len(arr)-1):
                if arr[i]>=arr[i+1]:
                    return False
            return True

        
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:

                if isincreasing(nums[:i]+nums[i+1:]):
                    return True
                
                if isincreasing(nums[:i+1]+nums[i+2:]):
                    return True
                
                return False
        return True