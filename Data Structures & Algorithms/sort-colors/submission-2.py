class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED = 0
        WHITE = 1
        BLUE = 2

        #red white blue
        """
        sort all red, white and then blue or red + white -> blue
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] == RED:
                swap = nums[l]
                nums[l] = nums[r]
                nums[r] = swap
                l += 1
        for w in range(len(nums)):
            if nums[w] == WHITE:
                swap = nums[l]
                nums[l] = nums[w]
                nums[w]= swap
                l += 1
        for b in range(len(nums)):
            if nums[b] == BLUE:
                swap = nums[l]
                nums[l] = nums[b]
                nums[b] = swap
                l += 1
        