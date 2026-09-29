class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}

        for i in nums:
            count_map[i] = 1 + count_map.get(i, 0)
        
        import heapq
        heap = []
        for key, val in count_map.items():
            heapq.heappush(heap, (-val, key))

        res = []

        while len(res) != k:
            res.append(heapq.heappop(heap)[1])

        return res