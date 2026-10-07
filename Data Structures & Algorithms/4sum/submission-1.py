class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue
                l = k + 1
                r = n - 1
                while l < r:
                    cur_sum = nums[i] + nums[k] + nums[l] + nums[r]
                    if cur_sum == target:
                        res.append([nums[i], nums[k], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif target < cur_sum:
                        r -= 1
                    else:
                        l += 1
        return res