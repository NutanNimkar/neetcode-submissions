from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        max_len = 0
        maxf = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])


            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            max_len = max(r - l + 1, max_len)
        return max_len



