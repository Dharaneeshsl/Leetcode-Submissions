class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        data=sorted(arr)
        hs={}
        c=0
        for i in range(len(data)):
            if data[i] not in hs:
                hs[data[i]]=c+1
                c+=1

        res=[]
        for i in range(len(arr)):
            res.append(hs[arr[i]])
        
        return res