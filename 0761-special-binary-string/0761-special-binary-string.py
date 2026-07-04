class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        bal=0
        start=0
        parts=[]
        for i,c in enumerate(s):
            if c=="1":
                bal+=1
            else:
                bal-=1

            if bal==0:
                parts.append("1"+self.makeLargestSpecial(s[start+1:i])+"0")
                start=i+1
        parts.sort(reverse=True)
        return "".join(parts)