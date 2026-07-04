class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl=timeToLive
        self.d={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId]=currentTime+self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d and self.d[tokenId]>currentTime:
            self.d[tokenId]=currentTime+self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt=0
        for t in self.d.values():
            if t>currentTime:
                cnt+=1
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)