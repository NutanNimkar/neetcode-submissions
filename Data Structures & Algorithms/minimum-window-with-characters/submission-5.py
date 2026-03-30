# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "":
#             return ""
        
#         hash_t, hash_s = {}, {}
#         have, need = 0, len(t)

#         res, resLen = [-1, -1], float('inf')

#         for c in t:
#             if c not in hash_t:
#                 hash_t[c] = 1
#             else:
#                 hash_t[c] += 1
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             hash_s[c] = 1 + hash_s.get(c, 0)

#             if c in hash_t and hash_t[c] == hash_s[c]:
#                 have += 1

#             while have == need:
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = r - l + 1
#                 hash_s[s[l]] -= 1
#                 if s[l] in hash_t and hash_s[s[l]] < hash_t[s[l]]:
#                     have -= 1
#                 l += 1
#         l, r = res
#         return s[l: r + 1] if resLen != float('inf') else ""
                      
            
            
            
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

