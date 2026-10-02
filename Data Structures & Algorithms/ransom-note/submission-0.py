from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine_map = Counter(magazine)

        for c in ransomNote:
            if c in magazine_map and magazine_map[c] > 0:
                magazine_map[c] -= 1
            else:
                return False
        return True
            