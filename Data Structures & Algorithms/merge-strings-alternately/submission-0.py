class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        
        l = r = 0 
        res = []

        while l < len(word1) and r < len(word2):

            res.append(word1[l])
            l+= 1
            res.append(word2[r])
            r+= 1 
        
        if l == len(word1) and r < len(word2):
            res.append(word2[r:])
        elif r == len(word2) and l < len(word1):
            res.append(word1[l:])

        return "".join(res)
