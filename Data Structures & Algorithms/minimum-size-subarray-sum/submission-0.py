class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pos_inf = math.inf
        min_sub = float('inf')

        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]

                if cur_sum >= target:
                    min_sub = min(min_sub, len(nums[i:j+1]))
                    break
        return 0 if min_sub  == float('inf') else min_sub