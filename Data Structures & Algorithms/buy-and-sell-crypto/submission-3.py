class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 1
        res = 0
        while r < len(prices):
            if prices[l] <= prices[r] and r <= len(prices):
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        return res
            



        















        # if not prices:
        #     return 0
        
        # min_price = float('inf')
        # max_profit = 0
        
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > max_profit:
        #         max_profit = price - min_price
        
        # return max_profit
                    



