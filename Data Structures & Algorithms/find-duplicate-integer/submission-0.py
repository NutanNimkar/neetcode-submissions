class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        l = 0

        while l < len(nums):
            for r in range (len(nums)):
                if nums[l] == nums[r] and l != r:
                    return nums[l]
            l += 1
        
        return 0

