class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        #down, up, right, left
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        visited = set()
        islands = 0

        def dfs(r, c):
            if(0 <= r < rows and 0 <= c < cols and 
            (r,c) not in visited and not grid[r][c] == "0"):
                visited.add((r,c))
                print(r, c)
                for i, j in directions:
                    dfs(r + i, c + j)
            else:
                return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r , c) not in visited:
                    dfs(r , c)
                    islands += 1
                
        return islands


            


                