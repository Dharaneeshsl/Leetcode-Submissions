class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        from collections import Counter
        res = 0
        for num, freq in Counter(nums).items():
            if freq == 2:
                res ^= num
        return res
