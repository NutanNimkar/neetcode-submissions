class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        frequencies = []

        i = 0

        while i < len(nums):
            j = i

            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            # nums[i] appears j - i times
            frequencies.append((j - i, nums[i]))

            i = j

        frequencies.sort(reverse=True)

        result = []

        for frequency, num in frequencies:
            result.append(num)

            if len(result) == k:
                break

        return result
