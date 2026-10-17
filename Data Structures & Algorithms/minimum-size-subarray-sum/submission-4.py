class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # min_sub = float('inf')

        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]

        #         if cur_sum >= target:
        #             min_sub = min(min_sub, len(nums[i:j+1]))
        #             break
        # return 0 if min_sub  == float('inf') else min_sub

        prefix = [0] * len(nums)
        min_length = float('inf')

        for i in range(len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        cur_sum = 0
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_length = min(min_length, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return 0 if min_length  == float('inf') else min_length

            