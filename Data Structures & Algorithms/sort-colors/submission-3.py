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

        def swap(i , j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        l = 0
        for r in range(len(nums)):
            if nums[r] == RED:
                swap(l,r)
                l += 1
        for w in range(len(nums)):
            if nums[w] == WHITE:
                swap(l,w)
                l += 1
        for b in range(len(nums)):
            if nums[b] == BLUE:
                swap(l,b)
                l += 1
        