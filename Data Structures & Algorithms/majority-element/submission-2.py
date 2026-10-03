from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums = Counter(nums)
        for key, value in nums.items():
            if value >= n // 2:
                return key

        return -1