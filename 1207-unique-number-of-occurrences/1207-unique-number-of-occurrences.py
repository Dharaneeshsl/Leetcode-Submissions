class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hs={}
        for i in range(len(arr)):
            hs[arr[i]]=hs.get(arr[i],0)+1

        count=set()
        for x in hs.values():
            if x in count:
                return False
            count.add(x)
        return True