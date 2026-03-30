class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        """
        brute is a triple for loop trying each comb for the triplets
        complexity: O(n3)
        space_complexity: O(n)

        """
        nums_sorted = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:

                cur_sum = nums_sorted[i] + nums_sorted[l] + nums_sorted[r]
                if cur_sum == 0:
                    res.add((nums_sorted[i], nums_sorted[l], nums_sorted[r]))
                    l += 1
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        return [list(i) for i in res]
                