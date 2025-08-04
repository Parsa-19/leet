class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices:
            
            if buy < sell:
                current_profit = sell - buy
                if current_profit > profit:
                    profit = current_profit
                continue

            buy = sell

        return profit



solu = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
res = solu.maxProfit(prices)
print(f"\nfucn returned: {res}")
        