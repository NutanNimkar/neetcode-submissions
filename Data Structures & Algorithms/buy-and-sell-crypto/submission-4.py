class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l, r = 0 , 1

        while l < r and r < len(prices):
            cur_profit = 0
            if prices[l] <= prices[r]:
                cur_profit = prices[r]  - prices[l]
                r += 1
            else:
                l = r
                r += 1
            max_profit = max(cur_profit, max_profit)
        return max_profit