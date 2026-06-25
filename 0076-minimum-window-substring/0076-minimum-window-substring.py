class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hs1 = {}
        for x in t:
            if x in hs1:
                hs1[x] += 1
            else:
                hs1[x] = 1

        hs2 = {}
        unique = len(hs1)   
        create = 0          

        l = 0
        mini = float('inf')
        start = 0

        for r in range(len(s)):
            c = s[r]
            if c in hs2:
                hs2[c] += 1
            else:
                hs2[c] = 1
            if c in hs1 and hs2[c] == hs1[c]:
                create += 1
            while l <= r and create == unique:
                if r - l + 1 < mini:
                    mini = r - l + 1
                    start = l
                left = s[l]
                hs2[left] -= 1

                if left in hs1 and hs2[left] < hs1[left]:
                    create -= 1

                l += 1

        if mini == float('inf'):
            return ""
        return s[start:start + mini]