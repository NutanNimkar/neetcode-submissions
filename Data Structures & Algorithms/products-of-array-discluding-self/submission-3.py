class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     res.append(prod)
        # return res

        """
        WE are using two precomputed arrays postfix, prefix.
        prefix will capture product of the array up until it
        postfix will caputure product of the array starting from the element without including it
        if i is index
        result = prefix[i-1] * postfix[i]
        """

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        

        return res 

