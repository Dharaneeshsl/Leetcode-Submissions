class Solution:
    def binaryGap(self, n: int) -> int:
        return max((j-i for i,j in zip([i for i,c in enumerate(bin(n)) if c=='1'], [i for i,c in enumerate(bin(n)) if c=='1'][1:])), default=0)