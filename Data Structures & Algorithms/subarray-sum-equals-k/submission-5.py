class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        do a nested loop counting each subarray
        and its sum and checking if its sum == k if it is we store the subarray in the list, if not we move and extend the subarray
        store it in a list 
        and return the length of the list in the end
        """
        # def get_sum(nums):
        #     sum = 0
        #     for i in nums:
        #         sum += i
        #     return sum

        # res = []
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         curSum = get_sum(nums[i:j+1])
        #         if curSum == k:
        #             res.append(nums[i:j+1])
        #         else:
        #             continue
        # return len(res)


        count = 0
        curSum = 0
        map  = {0: 1}

        for n in nums:

            curSum += n
            diff = curSum - k
            if diff in map:
                count += map[diff]
            map[curSum] = map.get(curSum, 0) + 1
        return count
        


                    
                