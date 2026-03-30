class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-f for f in freq.values()]  # Max-heap (store as negatives)
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # Store pairs: (remaining_count, ready_time)

        while maxHeap or cooldown:
            time += 1

            # Process next task if available
            if maxHeap:
                count = -1 * heapq.heappop(maxHeap) - 1
                if count > 0:
                    cooldown.append((count, time + n))  # Add to cooldown

            # Check if a task from cooldown is ready
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, -cooldown.popleft()[0])  # Re-add to heap

        return time