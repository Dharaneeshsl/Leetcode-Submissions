class Solution(object):
    def targetIndices(self, nums, target):
        smaller=0
        count=0
        for num in nums:
            if num<target:
                smaller+=1
            elif num == target:
                count+=1
        l=[]
        for i in range(smaller,smaller+count):
            l.append(i)
        return l
        