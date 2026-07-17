class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxi=0
        seen={}
        for right in range(len(s)):
            if s[right] in seen:
                left=max(left,seen[s[right]]+1)
            maxi=max(maxi,right-left+1)
            seen[s[right]]=right
        return maxi
