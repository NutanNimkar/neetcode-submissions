class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestPalindrome = ""
        resLen = 0

        for i in range(len(s)):
            l , r = i, i
            
            #odd length palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    print(l, r)
                    longestPalindrome = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                    
            #even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    longestPalindrome = s[l: r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1
        return longestPalindrome