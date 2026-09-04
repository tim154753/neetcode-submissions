class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        for i, price in enumerate(prices):
            if price < buy:
                buy = price
                sell = price
            elif price > sell:
                sell = price
            profit = max(profit, sell-buy)
        return profit
        