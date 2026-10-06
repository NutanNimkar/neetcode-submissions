class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        maxcount = 0
        for n in nums:
            count = 0
            if n - 1 not in nums_set:
                while n in nums_set:
                    n = n + 1
                    count += 1
            maxcount = max(maxcount, count)
        return maxcount

        