from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = Counter(nums)

        count_heap = [(-value, key) for key, value in count_map.items()]

        heapq.heapify(count_heap)


        final_list = []

        while k > 0:
            final_list.append(heapq.heappop(count_heap)[1])
            k -= 1
        return final_list