class OrderedStream:
    def __init__(self, n: int):
        self.stream=[""]*(n+1)
        self.ptr=1

    def insert(self, idKey: int, value: str):
        self.stream[idKey]=value
        ans=[]

        while self.ptr<len(self.stream) and self.stream[self.ptr]!="":
            ans.append(self.stream[self.ptr])
            self.ptr+=1

        return ans