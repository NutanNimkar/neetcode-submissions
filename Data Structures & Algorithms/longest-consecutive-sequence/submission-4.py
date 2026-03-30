class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_len = 0
        for val in nums:
            if (val - 1) not in nums_set:
                longest = 1
                while val + 1 in nums_set:
                    longest += 1
                    val += 1
                max_len = max(longest, max_len)
        return max_len
