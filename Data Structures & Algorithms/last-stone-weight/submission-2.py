import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            val1 = -1 * heapq.heappop(stones)
            val2 = -1 * heapq.heappop(stones)
            if val1 != val2:
                sub = val1 - val2
            if val1 == val2:
                sub = val1 - val2
            heapq.heappush(stones, -1 * sub)
        
        return -1 * stones[0]

        
            

