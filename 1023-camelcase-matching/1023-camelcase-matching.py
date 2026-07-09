class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(s):
            j=0
            for c in s:
                if j<len(pattern) and c==pattern[j]:
                    j+=1
                elif c.isupper():
                    return False
            return j==len(pattern)

        res=[]
        for s in queries:
            res.append(check(s))
        return res