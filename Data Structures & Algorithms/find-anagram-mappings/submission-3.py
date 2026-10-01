class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        numstopos = {nums2[i]: i for i in range(len(nums2))}


        mapping = [numstopos[num] for num in nums1]
        return mapping