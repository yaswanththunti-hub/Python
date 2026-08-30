class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if current_profit > profit:
                profit = current_profit
        return profit
s=Solution()
prices=[1,2,3,4,5,6,7]
print(s.maxProfit(prices))
