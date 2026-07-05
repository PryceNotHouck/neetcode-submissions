class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = prices[0]
        sell = prices[-1]
        for i, p in enumerate(prices):
            if not prices[i + 1:]:
                break
            if max(prices[i + 1:]) - p > sell - buy:
                buy = p
                sell = max(prices[i + 1:])
        
        return max(sell - buy, 0)