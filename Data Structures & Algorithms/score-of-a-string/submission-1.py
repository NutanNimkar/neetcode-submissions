class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        total_sum = 0

        while r < len(s):
            cur_diff = abs(ord(s[l]) - ord(s[r]))
            total_sum += cur_diff
            l += 1
            r += 1
        return total_sum
