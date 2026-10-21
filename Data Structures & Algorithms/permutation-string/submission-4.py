class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        n = len(s1)
        if n > len(s2):
            return False
        s1_count = Counter(s1)
        window = Counter(s2[:n])

        if window == s1_count:
            return True

        # for r in range(len(s2) - n + 1):
        #     substr = s2[r: r + n]
        #     if s1_count == Counter(substr):
        #         return True
        # return False  

        for r in range(n, len(s2)):

            window[s2[r]] += 1

            # remove the char leaving on the left
            left = s2[r - n]
            window[left] -= 1
            if window[left] == 0:
                del window[left]   # keep Counters comparable

            if window == s1_count:
                return True

        return False

                


