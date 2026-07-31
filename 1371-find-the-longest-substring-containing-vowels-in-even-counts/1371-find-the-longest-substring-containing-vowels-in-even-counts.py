class Solution:
    def findTheLongestSubstring(self,s:str)->int:
        pos={0:-1}
        mask=0
        ans=0
        mp={'a':0,'e':1,'i':2,'o':3,'u':4}
        for i,c in enumerate(s):
            if c in mp:
                mask^=1<<mp[c]
            if mask in pos:
                ans=max(ans,i-pos[mask])
            else:
                pos[mask]=i
        return ans