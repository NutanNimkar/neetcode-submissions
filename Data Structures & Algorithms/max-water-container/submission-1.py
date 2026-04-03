class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            index_diff = r - l
            cur_area = min(heights[l], heights[r]) * index_diff

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            res = max(cur_area, res)
        return res
