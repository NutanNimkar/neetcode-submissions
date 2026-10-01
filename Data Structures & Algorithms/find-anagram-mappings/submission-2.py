class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapping = []

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             mapping.append(j)
        #             break
        # return mapping
        numstopos = {nums2[i]: i for i in range(len(nums2))}

        for i in nums1:
            if i in numstopos:
                mapping.append(numstopos[i])
        return mapping