class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # num_set = set(nums)

        # if (len(num_set) != len(nums)):
        #     return True
        
        # return False
         
        hashm = {}

        for i in nums:
        
            if i not in hashm:
                hashm[i] = 1
            else:
                return True

        return False