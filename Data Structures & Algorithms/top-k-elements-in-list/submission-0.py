import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        max_heap = [(-freq, num) for num, freq in count.items()]

        heapq.heapify(max_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res
            
        

        
