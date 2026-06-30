class Solution(object):
    def mostFrequentEven(self, nums):
        freq={}
        for num in nums:
            if num%2==0:
                freq[num]=freq.get(num,0)+1
        ans=-1
        maxfreq=0
        for num,count in freq.items():
            if count>maxfreq:
                maxfreq=count
                ans=num
            elif count==maxfreq and num<ans:
                ans=num
        return ans