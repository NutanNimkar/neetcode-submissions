class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prevCourses = {}
        
        for i in range(numCourses):
            prevCourses[i] = []

        for crs, pre in prerequisites:
            prevCourses[crs].append(pre)
        

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prevCourses[crs] == []:
                return True
            
            visited.add(crs)
            for pre in prevCourses[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)

            prevCourses[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True            
            