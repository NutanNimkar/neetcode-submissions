from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = float('-inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            total_sum = max(cur_sum, total_sum)
            if cur_sum < 0:
                cur_sum = 0
        
        return total_sum
