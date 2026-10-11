class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        price, profit = float(inf), 0

        for num in prices:
            if num < price:
                price = num
            
            profit = max(profit, num- price)
        
        return profit