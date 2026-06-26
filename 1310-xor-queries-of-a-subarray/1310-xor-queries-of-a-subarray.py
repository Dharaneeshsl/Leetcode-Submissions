class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i]^=arr[i-1]
        ans=[]
        for l,r in queries:
            if l==0:
                ans.append(arr[r])
            else:
                ans.append(arr[r]^arr[l-1])
        return ans