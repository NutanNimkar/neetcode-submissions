class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        # 1, 2, 4, 5

        # 1, 2, 2 , 3, 3
        l , r = 0 , len(people) - 1
        res = 0
        while l <= r:
            curweight = people[l] + people[r]

            if curweight <= limit:
                res += 1
                r -= 1
                l += 1
            else:
                res += 1
                r -= 1
        return res
            
