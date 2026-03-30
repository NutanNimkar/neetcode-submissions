class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []

        while r < len(nums):
            window = nums[l:r + 1]
            window.sort()
            res.append(window[len(window) - 1])
            l+= 1
            r+= 1
        return res
            
