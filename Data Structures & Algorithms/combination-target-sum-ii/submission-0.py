class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(total, subset, start):
            if total == target:
                res.append(subset.copy())
                return
            
            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                subset.append(candidates[j])
                dfs(total + candidates[j], subset, j + 1)
                subset.pop()

                
        candidates.sort()
        res = []
        dfs(0, [], 0)
        return res


                    
            
            


