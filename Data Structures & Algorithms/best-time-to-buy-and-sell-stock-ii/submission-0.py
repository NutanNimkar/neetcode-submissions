class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 1
        maxProfit = 0

        while l < r and r < len(prices):
            profit = 0
            print(l)
            print("r", r)
            print(profit)
            if prices[l] >= prices[r]:
                l = r
                r += 1
            elif prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                l = r
                r += 1
            if l > 0:
                maxProfit = max(maxProfit, maxProfit + profit)
        return maxProfit
            
            