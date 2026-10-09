class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = -1
        max_profit = 0
        for i in range(len(prices)):
            if min_price == -1 or prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

        