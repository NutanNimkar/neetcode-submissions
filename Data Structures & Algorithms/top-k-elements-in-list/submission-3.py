from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = Counter(nums)


        count_heap = [(-val, key) for key, val in count_map.items()]

        heapq.heapify(count_heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(count_heap)[1])
            k -=1
        return res