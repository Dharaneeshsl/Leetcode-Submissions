class Solution:
    def commonChars(self,words:List[str])->List[str]:
        arr=[float('inf')]*26
        for word in words:
            cnt=[0]*26
            for ch in word:
                cnt[ord(ch)-97]+=1
            for i in range(26):
                arr[i]=min(arr[i],cnt[i])
        res=[]
        for i in range(26):
            res.extend([chr(i+97)]*arr[i])
        return res