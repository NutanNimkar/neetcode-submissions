from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # n = len(s1)

        # s1_count = Counter(s1)

        # for i in range(len(s2) - n + 1):

        #     substring = s2[i:i+n]

        #     if Counter(substring) == s1_count:
        #         return True
        # return False

        if len(s1) > len(s2):
            return False  

        s1_count = Counter(s1)
        n = len(s1)
        l = 0
        substring = ""

        for r in range(len(s2)):
                
            if s2[r] in s1_count:
                substring = s2[r: r+n]
            if Counter(substring) == s1_count:
                return True
        return False
