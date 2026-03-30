class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for num in nums:
            tmp = num * curMax
            curMax = max(num * curMin, num, num * curMax)
            curMin = min(tmp, curMin * num, num)
            res = max(curMax, res)
        return res
