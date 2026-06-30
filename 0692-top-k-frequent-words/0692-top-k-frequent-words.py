from collections import Counter
class Solution:
    def topKFrequent(self,words:List[str],k:int)->List[str]:
        freq=Counter(words)
        arr=[]
        for w in freq:
            arr.append((w,freq[w]))
        arr.sort(key=lambda x:(-x[1],x[0]))
        ans=[]
        for i in range(k):
            ans.append(arr[i][0])
        return ans