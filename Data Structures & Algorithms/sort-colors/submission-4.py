class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums) - 1
        i = 0
        RED = 0
        WHITE = 1
        BLUE = 2

        def swap(i , j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == RED:
                swap(l, i)
                l += 1
            elif nums[i] == BLUE:
                swap(r, i)
                r -= 1
                i -= 1
            i += 1
        
            

