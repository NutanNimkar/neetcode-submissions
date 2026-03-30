import heapq
class Solution:
    def findMin(self, nums: List[int]) -> int:
#so it runs only on rotated arrays 
# check for middle and see if the left most value is smaller than the middle value
# if it is search the right side, contains the min portion of the sorted arrata
# else search the left side contains the max portion of the array

        l , r = 0, len(nums) - 1
        while l != r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
                    
        return nums[l]