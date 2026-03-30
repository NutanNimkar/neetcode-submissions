class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time_elapsed = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
        
        while q:
            r, c, time = q.popleft()
            time_elapsed  = max(time, time_elapsed )
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr <ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    q.append((nr, nc, time + 1))
        return -1 if fresh_oranges > 0 else time_elapsed

            