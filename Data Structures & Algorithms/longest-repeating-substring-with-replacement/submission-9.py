class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # max_sub_len = 0

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         sub = s[i:j+1]
        #         replacements_needed = len(sub) - max(sub.count(c) for c in set(sub))
        #         if replacements_needed <= k:
        #             max_sub_len = max(len(sub), max_sub_len)
        # return max_sub_len
        # if len(s) <= 1:
        #     return 1
            
        count = {}
        l = 0
        max_sub_len = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            max_sub_len = max(max_sub_len, r - l + 1)
        return max_sub_len
