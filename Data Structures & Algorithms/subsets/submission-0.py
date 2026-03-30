class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i):
            # if i >= len(nums):
            res.append(path.copy())
                # return
            # path.append(nums[i])
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
            # for i in range(i, len(nums)):
            #     path.append(nums[i])
            # dfs(i + 1, path.append(nums[i]))
            # path.pop()
            # dfs(i + 1, path.append(nums[i]))
        
        dfs(0)
        return list(res)
            

            


            
            




        