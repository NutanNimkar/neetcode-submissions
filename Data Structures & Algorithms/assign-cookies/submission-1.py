class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        l = 0 # child point
        r = 0 # cookie
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                l += 1
            r += 1
        return l
            


