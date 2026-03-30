class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()

        res = 0
        adjList = {i: [] for i in range(n)}
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        def dfs(node):
            visit.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visit:
                    dfs(neighbor)
            return True
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res



