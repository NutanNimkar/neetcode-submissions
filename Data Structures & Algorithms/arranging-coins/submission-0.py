class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        i = 0
        while i < n:
            i += 1
            n -= i
        return i
