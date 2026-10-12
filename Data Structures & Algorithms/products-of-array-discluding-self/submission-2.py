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
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)


        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        

        return res 

