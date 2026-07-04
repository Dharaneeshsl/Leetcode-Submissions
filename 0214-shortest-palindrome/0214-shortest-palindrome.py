class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        t = s + "#" + r

        lps = [0] * len(t)
        j = 0

        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = lps[j - 1]
            if t[i] == t[j]:
                j += 1
                lps[i] = j

        k = lps[-1]
        return r[:len(s) - k] + s