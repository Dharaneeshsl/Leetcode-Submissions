class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        def merge(left,mid,right):
            nonlocal count
            j=mid+1
            for i in range(left,mid+1):
                while j<=right and nums[i]>2*nums[j]:
                    j+=1
                count+=j-(mid+1)
            temp=[]
            i=left
            j=mid+1
            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=right:
                temp.append(nums[j])
                j+=1
            nums[left:right+1]=temp
        def mergeSort(left,right):
            if left>=right:
                return
            mid=(left+right)//2
            mergeSort(left,mid)
            mergeSort(mid+1,right)
            merge(left,mid,right)

        mergeSort(0,len(nums)-1)
        return count