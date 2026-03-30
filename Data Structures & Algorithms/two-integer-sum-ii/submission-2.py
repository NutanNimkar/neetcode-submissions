class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, 1

        while l < r:
            if r < len(numbers) and target == numbers[l] + numbers[r]:
                return [l + 1, r + 1]
            elif r != len(numbers):
                r += 1
            else:
                l+= 1
                r = l + 1
        
        """
        above solution may work but its bad because it iterating through the list n2 times
        """

        # l, r = 0, len(numbers) - 1

        # while l < r:
        #     cur_index_sum = numbers[l] + numbers[r]
        #     if cur_index_sum == target:
        #         return [l + 1, r + 1]
        #     elif cur_index_sum < target:
        #         l += 1
        #     else:
        #         r -= 1