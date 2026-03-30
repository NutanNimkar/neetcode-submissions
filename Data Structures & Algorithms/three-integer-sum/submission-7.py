class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        """
        brute is a triple for loop trying each comb for the triplets
        complexity: O(n3)
        space_complexity: O(n)

        """
        nums_sorted = sorted(nums)
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            while l < r:
                cur_sum = nums_sorted[i] + nums_sorted[l] + nums_sorted[r]
                if cur_sum == 0:
                    res.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    l += 1
                    r -= 1
                    while l < r and nums_sorted[l] == nums_sorted[l - 1]:
                        l+=1
                    while l < r and nums_sorted[r] == nums_sorted[r + 1]:
                        r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res
