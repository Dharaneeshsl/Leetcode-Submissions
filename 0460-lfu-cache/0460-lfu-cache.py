from collections import defaultdict,OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.val={}
        self.cnt={}
        self.freq=defaultdict(OrderedDict)
        self.minFreq=0

    def get(self, key: int) -> int:
        if key not in self.val:
            return -1
        f=self.cnt[key]
        del self.freq[f][key]
        if not self.freq[f]:
            del self.freq[f]
            if self.minFreq==f:
                self.minFreq+=1
        self.cnt[key]=f+1
        self.freq[f+1][key]=0
        return self.val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.val:
            self.val[key]=value
            self.get(key)
            return
        if len(self.val)==self.cap:
            k,_=self.freq[self.minFreq].popitem(last=False)
            del self.val[k]
            del self.cnt[k]
        self.val[key]=value
        self.cnt[key]=1
        self.freq[1][key]=0
        self.minFreq=1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)