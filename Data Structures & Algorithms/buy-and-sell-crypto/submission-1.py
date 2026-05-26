class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        profit = 0

        while s<len(prices):
            if prices[b] > prices[s]:
                b = s
            profit = max(profit, prices[s]-prices[b])
            s += 1
        return profit