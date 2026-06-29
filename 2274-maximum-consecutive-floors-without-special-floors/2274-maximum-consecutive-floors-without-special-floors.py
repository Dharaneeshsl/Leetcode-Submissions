class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        ans=special[0]-bottom
        for i in range(1,len(special)):
            ans=max(ans,special[i]-special[i-1]-1)
        ans=max(ans,top-special[-1])
        return ans