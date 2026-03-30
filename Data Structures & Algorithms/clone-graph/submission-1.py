"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None



        # if not node:
        #     return None

        # stack = []
        # seen = set()
        # graphCopy = {}

        # stack.append(node)
        # graphCopy[node] = Node(node.val)

        # if not node.neighbors:
        #     graphCopy[node] = Node(node.val)
            

        # while stack:
        #     node = stack.pop()

        #     seen.add(node)
        #     for neighbor in node.neighbors:
        #         if neighbor not in seen:
        #             if neighbor not in graphCopy:
        #                 graphCopy[neighbor] = Node(neighbor.val)
        #                 stack.append(neighbor)
        #         graphCopy[node].neighbors.append(graphCopy[neighbor])
            
        
        # return graphCopy[node]
        
        
                


            