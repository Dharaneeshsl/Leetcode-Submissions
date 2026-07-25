class SmallestInfiniteSet:

    def __init__(self):
        self.curr=1
        self.heap=[]
        self.seen=set()

    def popSmallest(self) -> int:
        if self.heap:
            x=heappop(self.heap)
            self.seen.remove(x)
            return x
        x=self.curr
        self.curr+=1
        return x

    def addBack(self, num: int) -> None:
        if num<self.curr and num not in self.seen:
            heappush(self.heap,num)
            self.seen.add(num)