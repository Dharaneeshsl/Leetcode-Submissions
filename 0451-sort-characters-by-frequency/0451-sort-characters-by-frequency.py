class Solution(object):
    def frequencySort(self, s):
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        arr=[]
        for i,count in freq.items():
            arr.append((count,i))
        arr.sort(reverse=True)
        s=""
        for count,i in arr:
            s+=count*i
        return s