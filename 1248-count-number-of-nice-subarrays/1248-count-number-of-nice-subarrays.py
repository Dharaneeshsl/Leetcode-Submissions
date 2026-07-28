class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        odd = 0
        ans = 0
        for x in nums:
            if x % 2:
                odd += 1
            if odd-k in freq:
                ans += freq[odd-k]
            freq[odd] = freq.get(odd,0)+1
        return ans