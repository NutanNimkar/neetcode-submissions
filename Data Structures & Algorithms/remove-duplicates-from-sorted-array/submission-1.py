class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique = sorted(list(set(nums)))
        # nums[:len(unique)] = unique
        # return len(unique)

        l , r = 0, 1

        while l < r and r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                l+= 1
                nums[l] = nums[r]
                r += 1
        return l + 1