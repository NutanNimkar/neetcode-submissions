class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]


        for word in strs[1:]:
            c = 0
            while c < len(word) and c < len(common_prefix):
                if common_prefix[c] != word[c]:
                    break
                c += 1
            common_prefix = common_prefix[:c]

        return common_prefix
