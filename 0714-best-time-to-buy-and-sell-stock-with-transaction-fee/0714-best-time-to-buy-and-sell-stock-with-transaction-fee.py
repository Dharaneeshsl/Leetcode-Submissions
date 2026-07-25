class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold=-prices[0]
        cash=0
        for price in prices[1:]:
            prevHold=hold
            hold=max(hold,cash-price)
            cash=max(cash,prevHold+price-fee)

        return cash