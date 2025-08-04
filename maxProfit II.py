class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profits = 0

        for sell in prices:
            
            if buy < sell:
                current_profit = sell - buy
                profits += current_profit
                
            buy = sell

        return profits



solu = Solution()
prices = [7,1,5,3,6,4]
res = solu.maxProfit(prices)
print(f"\nfucn returned: {res}")
        