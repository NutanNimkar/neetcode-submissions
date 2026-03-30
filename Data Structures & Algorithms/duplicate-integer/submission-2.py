class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         hashm = {}

         for n in nums:
            if n not in hashm:
                hashm[n] = 1
            else:
                return True
         return False