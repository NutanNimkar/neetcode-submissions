class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        string_map = Counter(s)


        for c in range(len(s)):
            if s[c] in string_map and string_map[s[c]] == 1:
                return c
        return -1
            
