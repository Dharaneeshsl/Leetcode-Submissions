class CustomStack:

    def __init__(self, maxSize: int):
        self.k=maxSize
        self.stack=[0]*maxSize
        self.inc=[0]*maxSize
        self.top=-1

    def push(self, x: int) -> None:
        if self.top==self.k-1:
            return
        self.top+=1
        self.stack[self.top]=x

    def pop(self) -> int:
        if self.top==-1:
            return -1

        i=self.top
        res=self.stack[i]+self.inc[i]
        if i>0:
            self.inc[i-1]+=self.inc[i]

        self.inc[i]=0
        self.top-=1

        return res

    def increment(self, k: int, val: int) -> None:
        if self.top==-1:
            return
        idx=min(k-1,self.top)
        self.inc[idx]+=val  
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)