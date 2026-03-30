class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visit = set()
        adjList = {i:[] for i in range(n)}

        
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        prev = -1

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for ed in adjList[node]:
                if ed == parent:
                    continue
                if not dfs(ed, node):
                    return False
            return True
            
        if not dfs(0, -1):
            return False

        return len(visit) == n