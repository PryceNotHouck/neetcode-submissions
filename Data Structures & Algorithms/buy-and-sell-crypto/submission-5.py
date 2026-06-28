class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = len(prices) - 1

        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            if prices[1] - prices[0] > 0:
                return prices[1] - prices[0]
            else:
                return 0

        minimum = 0
        for front, p in enumerate(prices[::-1]):
            back = len(prices) - (front + 1)
            
            try:
                if len(prices[:back]):
                    minimum = min(prices[:back])
            except ValueError:
                pass

            if prices[back] - minimum > prices[sell] - prices[buy]:
                sell = back
                buy = prices.index(minimum)

        if prices[sell] - prices[buy] > 0:
            return prices[sell] - prices[buy]
        else:
            return 0