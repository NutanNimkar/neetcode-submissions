class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        def dfs(start, subset):
            if start == len(s):
                res.append(subset.copy())
                return 
                
            for i in range(start, len(s)):
                if not self.isPalindrome(s[start:i+1]):
                    continue
                subset.append(s[start:i+1])
                dfs(i + 1, subset)
                subset.pop()
        
        dfs(0, [])
        return res

    def isPalindrome(self, word):
        l , r = 0 , len(word) - 1

        while l <= r :
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
