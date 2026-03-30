class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visited or 
                        grid[r + dr][c + dc] == 1):
                            continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            length += 1
        return -1