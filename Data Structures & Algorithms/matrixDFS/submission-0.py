class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_paths = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1 or (r, c) in visited:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            visited.add((r, c))
            paths = 0
            for dr, dc in directions:
                paths += dfs(r + dr, c + dc)
            visited.remove((r, c))
            return paths
        return dfs(0, 0)
            