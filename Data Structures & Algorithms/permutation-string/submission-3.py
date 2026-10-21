class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        n = len(s1)
        if n > len(s2):
            return False
        s1_count = Counter(s1)

        for r in range(len(s2) - n + 1):
            substr = s2[r: r + n]
            if s1_count == Counter(substr):
                return True
        return False
